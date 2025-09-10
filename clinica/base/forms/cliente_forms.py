import re

from django import forms
from django.forms.widgets import DateInput, TextInput

from clinica.base.models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'cpf', 'telefone', 'data_nascimento']
        widgets = {
            'data_nascimento': DateInput(attrs={'type': 'date'}),
            'cpf': TextInput(attrs={
                'placeholder': '000.000.000-00',
                'maxlength': '14',
                'pattern': r'\d{3}\.\d{3}\.\d{3}-\d{2}',
                'title': 'Digite o CPF no formato 000.000.000-00'

            }),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        return re.sub(r'\D', '', cpf)  # remove tudo que não for número
