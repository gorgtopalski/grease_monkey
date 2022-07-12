from datetime import date
from django import forms

from context import models
from django.contrib.auth.models import User

from working_shift.models import WorkingShift 

class UserModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.get_full_name()

class DateInput(forms.DateInput):
    input_type = 'date'

class ShiftChangeForm(forms.ModelForm):
    class Meta:
        model = WorkingShift
        fields = '__all__'
    
    users = User.objects.all().filter(is_superuser=False).order_by('first_name')

    specialist_vc1 = UserModelChoiceField(users, required=False, label='Especialista VC')
    specialist_vc2 = UserModelChoiceField(users, required=False, label='Especialista VC')
    team = forms.ModelChoiceField(models.Team.objects.all(), required=True, label='Equipo') 
    shift = forms.ModelChoiceField(models.Shift.objects.all(), required=True, label='Turno')  
    date = forms.DateField(required=True, label='Fecha', widget=DateInput, initial=date.today())