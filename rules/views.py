from re import template
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import DetailView, ListView
from models.models import Production
from rules.forms import RulesForm

from rules.models import Rules

# Create your views here.

class RulesCreateView(CreateView):
    model = Rules
    form_class = RulesForm

    def get_initial(self):
        initial = super().get_initial()

        if 'production' in self.kwargs:
            key = self.kwargs['production']
            if (key != 0):
                production = get_object_or_404(Production, pk = key)
                initial['production'] = production.id

        return initial
        

class RulesUpdateView(UpdateView):
    model = Rules
    form_class = RulesForm

    def get_initial(self):
        initial = super().get_initial()

        if 'production' in self.kwargs:
            key = self.kwargs['production']
            if (key != 0):
                production = get_object_or_404(Production, pk = key)
                initial['production'] = production.id

        return initial



class RulesDetailsView(DetailView):
    model = Rules
    fields = '__all__'

    def get_object(self):
        if 'production' in self.kwargs:
            key = self.kwargs['production']
            if (key != 0):
                production = get_object_or_404(Production, pk = key)
                return Rules.objects.filter(production=production).first()



class RulesListView(ListView):
    model = Rules
    fields = '__all__'

    def get_queryset(self):
        qs = super().get_queryset()
        active = Production.objects.filter(finished=False).all()
        qs = qs.filter(production__in=active)
        return qs


class SelectProductionToCreateRuleView(ListView):
    template_name_suffix = '_rules_select'
    
    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        return Production.objects.filter(finished=False).order_by('line')
    