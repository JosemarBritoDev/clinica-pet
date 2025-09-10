from django import forms
from clinica.base.templatetags import meus_filtros


# 🔍 Testes para format_cpf
def test_format_cpf_valido():
    cpf = "12345678901"
    resultado = meus_filtros.format_cpf(cpf)
    assert resultado == "123.456.789-01"


def test_format_cpf_com_pontuacao():
    cpf = "123.456.789-01"
    resultado = meus_filtros.format_cpf(cpf)
    assert resultado == "123.456.789-01"


def test_format_cpf_invalido():
    cpf = "12345678"
    resultado = meus_filtros.format_cpf(cpf)
    assert resultado == "12345678"


# 🎨 Teste para addclass
class DummyForm(forms.Form):
    nome = forms.CharField()


def test_addclass_aplica_css():
    form = DummyForm()
    campo = form['nome']
    widget_html = meus_filtros.addclass(campo, 'form-control')
    assert 'class="form-control"' in widget_html
