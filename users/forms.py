from django import forms

class UserCreateForm(forms.Form):
    first_name = forms.CharField(label='Nombre', max_length=100)
    last_name = forms.CharField(label='Apellidos', max_length=100)