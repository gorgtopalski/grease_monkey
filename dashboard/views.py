
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, TemplateView
from context.models import Shift, Team
from dashboard.forms import ShiftChangeForm

from models.models import Production
from django.contrib.auth.models import User

# Create your views here.

class DashboardView(ListView):
    model = Production
    fields = '__all__'
    template_name = 'dashboard/home.html'

    def translate_session(self):
        data = {}

        if self.request.session.get('specialist_vc1', 0):
            pk = self.request.session.get('specialist_vc1')
            user = User.objects.get(pk=pk)
            data['specialist_vc1'] = user.get_full_name()

        if self.request.session.get('specialist_vc2', 0):
            pk = self.request.session.get('specialist_vc2')
            user = User.objects.get(pk=pk)
            data['specialist_vc2'] = user.get_full_name()

        if self.request.session.get('team'):
            pk = self.request.session.get('team')
            team = Team.objects.get(pk=pk)
            data['team'] = team

        if self.request.session.get('shift'):
            pk = self.request.session.get('shift')
            shift = Shift.objects.get(pk=pk)
            data['shift'] = shift

        if self.request.session.get('date'):
            data['date'] = self.request.session.get('date')

        return data    
        
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(finished=False).order_by('line')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.translate_session()
        
        return context


def shift_change(request):
    if request.method == 'POST':
        form = ShiftChangeForm(request.POST)
        if form.is_valid():
            request.session.flush()

            if form.cleaned_data['specialist_vc1'] == None:
                request.session['specialist_vc1'] = 0
            else:
                request.session['specialist_vc1'] = form.cleaned_data['specialist_vc1'].id

            if form.cleaned_data['specialist_vc2'] == None:
                request.session['specialist_vc2'] = 0
            else:
                request.session['specialist_vc2'] = form.cleaned_data['specialist_vc2'].id

            request.session['team'] = form.cleaned_data['team'].id
            request.session['shift'] = form.cleaned_data['shift'].id
            request.session['date'] = form.cleaned_data['date'].strftime('%d/%m/%Y')
            return redirect('dashboard:home')
    else:
        form = ShiftChangeForm()

    return render(request, 'dashboard/shift_change.html', {'form': form })
