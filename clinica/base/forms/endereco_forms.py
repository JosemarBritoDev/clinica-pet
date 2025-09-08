from django import forms

from clinica.base.models import EnderecoCliente


class EnderecoClienteForm(forms.ModelForm):
    class Meta:
        model = EnderecoCliente
        fields = ['rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep']
