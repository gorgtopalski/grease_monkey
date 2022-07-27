from django import forms

from rules.models import Rules


class RulesForm(forms.ModelForm):
    class Meta:
        model = Rules
        fields = '__all__'
        widgets = {
            'production': forms.TextInput(attrs={'readonly': '', 'hidden': ''},),
        }
        