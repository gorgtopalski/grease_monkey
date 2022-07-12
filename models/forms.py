from dataclasses import field
from django import forms

from models.models import Production


class DateInput(forms.DateInput):
    input_type = 'date'


class ProductionCreateForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = '__all__'
        widgets = {
            "start_date": DateInput(),
            "end_date": DateInput(),
        }
