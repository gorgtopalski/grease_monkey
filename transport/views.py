from dataclasses import field
from datetime import datetime
from urllib import request
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.urls import reverse
from context.models import Line
from models.models import Production
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import ListView, DetailView, TemplateView

from transport.forms import TransportForm
from transport.models import TransportControl

# Create your views here.

def tranport_control(request):
    shift_id = request.session.get('working_shift_id', 0)
    if shift_id != 0:
        control = TransportControl.objects.filter(working_shift=shift_id).first()

        if control is None:
            return redirect('transport:control-create')
        else:
            return redirect('transport:control-update', control.id)
    else:
        return redirect('dashboard:home')


class TransportControlListView(ListView):
    model = TransportControl
    fields = '__all__'
    template_name = 'transport/transport_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id')
        return qs


class TransportControlUpdateView(UpdateView):
    model = TransportControl
    form_class = TransportForm
    template_name = 'transport/transport_control.html'
    success_url = '/'
    extra_context = { 'update': True }


class TransportControlCreateView(CreateView):
    model = TransportControl
    form_class = TransportForm
    template_name = 'transport/transport_control.html'
    success_url = '/'

    def get_initial(self):
        active = Production.objects.filter(finished=False).all()
        lines = Line.objects.all()
        values = {}
     
        l11 = lines.filter(line='L11').get().id
            
        if active.filter(line=l11).exists():
            values['production_l11a'] = active.filter(line=l11).get().id
            values['production_l11b'] = active.filter(line=l11).get().id
        else:
            l11a = lines.filter(line='L11A').get().id
            if active.filter(line=l11a).exists:
                values['production_l11a'] = active.filter(line=l11a).get().id

            l11b = lines.filter(line='L11B').get().id
            if active.filter(line=l11b).exists:
                values['production_l11b'] = active.filter(line=l11b).get().id


        l14 = lines.filter(line='L14').get().id
        if active.filter(line=l14).exists():
            values['production_l14'] = active.filter(line=l14).get().id


        l12 = lines.filter(line='L12').get().id
        if active.filter(line=l12).exists():
            values['production_l12'] = active.filter(line=l12).get().id


        l13 = lines.filter(line='L13').get().id
        if active.filter(line=l13).exists():
            values['production_l13'] = active.filter(line=l13).get().id


        initial_data = {}
        initial_data['working_shift'] = self.request.session.get('working_shift_id', 0)
        initial_data['date'] = datetime.now()
        initial_data.update(values)

        return initial_data

 
# def tranport_control(request):

#     #TODO: cleanup!!!
#     def get_productions():
#         active = Production.objects.filter(finished=False).all()
#         lines = Line.objects.all()
#         values = {}
     
#         l11 = lines.filter(line='L11').get().id
            
#         if active.filter(line=l11).exists():
#             values['production_l11a'] = active.filter(line=l11).get().id
#             values['production_l11b'] = active.filter(line=l11).get().id
#         else:
#             l11a = lines.filter(line='L11A').get().id
#             if active.filter(line=l11a).exists:
#                 values['production_l11a'] = active.filter(line=l11a).get().id

#             l11b = lines.filter(line='L11B').get().id
#             if active.filter(line=l11b).exists:
#                 values['production_l11b'] = active.filter(line=l11b).get().id


#         l14 = lines.filter(line='L14').get().id
#         if active.filter(line=l14).exists():
#             values['production_l14'] = active.filter(line=l14).get().id


#         l12 = lines.filter(line='L12').get().id
#         if active.filter(line=l12).exists():
#             values['production_l12'] = active.filter(line=l12).get().id


#         l13 = lines.filter(line='L13').get().id
#         if active.filter(line=l13).exists():
#             values['production_l13'] = active.filter(line=l13).get().id
        
#         return values

#     def get_initial_form_data():
#         initial_data = {}
#         initial_data['working_shift'] = request.session.get('working_shift_id', 0)
#         initial_data['date'] = datetime.now()
#         initial_data.update(get_productions())  

#         return initial_data

#     def get_data_for_current_shift():
#         shift_id = request.session.get('working_shift_id', 0)
#         if shift_id != 0:
#             control = TransportControl.objects.filter(working_shift=shift_id).first()
#             if control:
#                 return control
#             else:
#                 return None

#     if request.method == 'POST':
#         current = get_data_for_current_shift()
#         # this will create a new transport control
#         if current is None:
#             form = TransportForm(request.POST, initial=get_initial_form_data())
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'Control de transporte guardado!')
#                 return redirect('dashboard:home')
#         else:
#             # this will update the current control
#             form = TransportForm(request.POST, instance=current)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'Control de transporte actualizado!')
#                 return redirect('dashboard:home')
#     else:
#         current = get_data_for_current_shift()

#         if current is None:
#             form = TransportForm()
#             form.initial = get_initial_form_data()
#             update = False
#         else:
#             form = TransportForm(instance=current)
#             update = True

#         return render(request, 'transport/transport_control.html', {'form': form, 'update': update})

#     messages.error(request, form.errors)
#     return redirect('dashboard:home')