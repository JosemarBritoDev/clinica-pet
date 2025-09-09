import pytest
from django.core import exceptions

from clinica.base.models import Cliente, EnderecoCliente


@pytest.mark.django_db
def test_criar_cliente_com_endereco():
    endereco = EnderecoCliente.objects.create(
        rua="Rua das Palmeiras",
        numero=123,
        complemento="Apto 101",
        bairro="Centro",
        cidade="São Paulo",
        estado="SP",
        cep="01000-000"
    )

    cliente = Cliente.objects.create(
        nome="Josemar",
        cpf="12345678900",
        email="josemar@example.com",
        endereco=endereco,
        telefone="(11)91234-5678",
        data_nascimento="1990-01-01"
    )

    assert Cliente.objects.count() == 1
    assert cliente.endereco.rua == "Rua das Palmeiras"
    assert cliente.cpf == "12345678900"


def test_cliente_str(db):
    endereco = EnderecoCliente.objects.create(
        rua="Rua A", numero=1, complemento="", bairro="B", cidade="C", estado="SP",
        cep="01000-000"
    )
    cliente = Cliente.objects.create(
        nome="Josemar", cpf="12345678900", email="j@example.com",
        endereco=endereco, telefone="(11)91234-5678", data_nascimento="1990-01-01"
    )
    assert str(cliente) == "Josemar"


def test_endereco_cep_invalido(db):
    with pytest.raises(exceptions.ValidationError):
        endereco = EnderecoCliente(
            rua="Rua A", numero=1, complemento="", bairro="B",
            cidade="C", estado="SP", cep="1234567"  # CEP inválido
        )
        endereco.full_clean()  # dispara validações do modelo


def test_cliente_sem_nome(db):
    endereco = EnderecoCliente.objects.create(
        rua="Rua A", numero=1, complemento="", bairro="B", cidade="C", estado="SP",
        cep="01000-000"
    )
    cliente = Cliente(
        cpf="12345678900", email="j@example.com",
        endereco=endereco, telefone="(11)91234-5678", data_nascimento="1990-01-01"
    )
    with pytest.raises(exceptions.ValidationError):
        cliente.full_clean()
