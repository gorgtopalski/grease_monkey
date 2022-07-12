from datetime import date
from unicodedata import name
from urllib import request
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import ListView, DetailView, TemplateView
from models.forms import ProductionCreateForm
from django.db.models import Q
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from django.core import serializers

from models.models import BottleModel, Production
from context.models import Color, Line
# Create your views here.


class ModelCreateView(CreateView):
    model = BottleModel
    fields = '__all__'


class ModelUpdateView(UpdateView):
    model = BottleModel
    fields = '__all__'
    template_name_suffix = "_update_form"


class ModelListView(ListView):
    model = BottleModel
    fields = '__all__'


class ModelDetailView(DetailView):
    model = BottleModel
    fields = '__all__'


class ProductionDetailView(DetailView):
    model = Production
    fields = '__all__'


class ProductionListView(TemplateView):
    template_name = 'models/production_list.html'


class ProductionListViewJson(BaseDatatableView):
    model = Production
    columns = ['line', 'model', 'color', 'start_date', 'end_date', 'finished']
    max_display_length = 500

    def filter_queryset(self, qs):
        print(self.request.POST)
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(model__name__contains=search) | Q(model__blueprint__contains=search))
            
        return qs


class ProductionCreateView(CreateView):
    model = Production
    form_class = ProductionCreateForm

    def get_initial(self):
        initial = super().get_initial()

        if (self.kwargs['production'] != 0):
            production = get_object_or_404(Production, pk=self.kwargs['production'])
            production.end_date = date.today()
            production.finished = True
            production.save()
            initial['color'] = production.color.id

        if (self.kwargs['model'] != 0):
            model = get_object_or_404(BottleModel, pk=self.kwargs['model'])
            initial['model'] = model.id

        if (self.kwargs['line'] !=0):
            line = get_object_or_404(Line, pk=self.kwargs['line'])
            initial['line'] = line.id
            
        initial['start_date'] = date.today()
        return initial
   

class ProductionUpdateView(UpdateView):
    model = Production
    fields = '__all__'
    template_name_suffix = "_update_form"


class ProductionJobChange(ListView):
    model = Production
    template_name_suffix = "_change"

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        qs = super().get_queryset()
        qs = qs.filter(finished=False).order_by('line')

        return qs