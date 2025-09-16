from django import forms
from django.forms.widgets import DateInput
from ..models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['nome', 'nascimento', 'categoria', 'cor']
        widgets = {
            'nascimento': DateInput(attrs={'type': 'date'})
        }
        exclude = ['dono', ]
