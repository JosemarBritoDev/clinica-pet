from django import forms

from clinica.base.models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'cpf', 'telefone', 'data_nascimento']

