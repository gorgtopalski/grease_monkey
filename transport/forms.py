import re
from django import forms

from transport.models import TransportControl

class RadioSelectGroup(forms.RadioSelect):
    template_name = 'transport/widgets/radio_select.html'

class TransportForm(forms.ModelForm):
    class Meta:
        model = TransportControl
        fields = '__all__'
        widgets = {
            'working_shift': forms.TextInput(attrs={'readonly': ''},),
            'production_l11a': forms.TextInput(attrs={'readonly': '', 'hidden': ''},),
            'production_l11b': forms.TextInput(attrs={'readonly': '', 'hidden': ''},),
            'production_l14': forms.TextInput(attrs={'readonly': '', 'hidden': ''},),
            'production_l12': forms.TextInput(attrs={'readonly': '', 'hidden': ''},),
            'production_l13': forms.TextInput(attrs={'readonly': '', 'hidden': ''},),
        }

    CHOICES = ((True, 'OK'), (False, 'KO'))

    convoyer_l11a = forms.ChoiceField(

        widget=RadioSelectGroup,
        choices=CHOICES,
        required=False,
        initial=3
    )

    convoyer_l11b = forms.ChoiceField(

        widget=RadioSelectGroup,
        choices=CHOICES,
        required=False,
        initial=3
    )

    wheel_l11 = forms.ChoiceField(
        widget=RadioSelectGroup,
        choices=CHOICES,
        required=False,
        initial=3
    )

    cross_l11 = forms.ChoiceField(
        widget=RadioSelectGroup,
        choices=CHOICES,
        required=False,
        initial=3
    )

    lehr_l11 = forms.ChoiceField(
        widget=RadioSelectGroup,
        choices=CHOICES,
        required=False,
        initial=3
    )

    # l14

    convoyer_l14 = forms.ChoiceField(
        widget=RadioSelectGroup,
        choices=CHOICES,
        required=False,
        initial=3
    )

    wheel_l14 = forms.ChoiceField(
        widget=RadioSelectGroup,
        choices=CHOICES,
        required=False,
        initial=3
    )

    cross_l14 = forms.ChoiceField(
        widget=RadioSelectGroup,
        choices=CHOICES,
        required=False,
        initial=3
    )

    lehr_l14 = forms.ChoiceField(
        widget=RadioSelectGroup,
        choices=CHOICES,
        required=False,
        initial=3
    )

    # l12

    convoyer_l12a = forms.ChoiceField(
        widget=RadioSelectGroup,
        choices=CHOICES,
        required=False,
        initial=3
    )

    convoyer_l12b = forms.ChoiceField(
        widget=RadioSelectGroup,
        choices=CHOICES,
        required=False,
        initial=3
    )

    wheel_l12 = forms.ChoiceField(
        widget=RadioSelectGroup,
        choices=CHOICES,
        required=False,
        initial=3
    )

    cross_l12 = forms.ChoiceField(
        widget=RadioSelectGroup,
        choices=CHOICES,
        required=False,
        initial=3
    )

    lehr_l12 = forms.ChoiceField(
        widget=RadioSelectGroup,
        choices=CHOICES,
        required=False,
        initial=3
    )

    # l13

    convoyer_l13 = forms.ChoiceField(
        widget=RadioSelectGroup,
        choices=CHOICES,
        required=False,
        initial=3
    )

    wheel_l13 = forms.ChoiceField(
        widget=RadioSelectGroup,
        choices=CHOICES,
        required=False,
        initial=3
    )

    cross_l13 = forms.ChoiceField(
        widget=RadioSelectGroup,
        choices=CHOICES,
        required=False,
        initial=3
    )

    lehr_l13 = forms.ChoiceField(
        widget=RadioSelectGroup,
        choices=CHOICES,
        required=False,
        initial=3
    )
