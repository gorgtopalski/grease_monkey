
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, TemplateView

from models.models import Production

from working_shift.models import WorkingShift

# Create your views here.

class DashboardView(ListView):
    model = Production
    fields = '__all__'
    template_name = 'dashboard/home.html'

    def get_working_shift(self):
        pk = self.request.session.get('working_shift_id', 0)
        if pk != 0:
            return WorkingShift.objects.get(pk=pk)
        else:
            return None
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(finished=False).order_by('line')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['working_shift'] = self.get_working_shift()
        
        return context