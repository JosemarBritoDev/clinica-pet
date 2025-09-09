import pytest
from clinica.base.models import Cliente, EnderecoCliente
from clinica.base.services.cliente_service import cadastrar_cliente
from clinica.base.services.endereco_service import cadastrar_endereco


@pytest.mark.django_db
def test_cadastrar_endereco_salva_no_banco():
    endereco_data = EnderecoCliente(
        rua="Rua das Palmeiras",
        numero=123,
        complemento="Apto 101",
        bairro="Centro",
        cidade="São Paulo",
        estado="SP",
        cep="01000-000"
    )
    endereco = cadastrar_endereco(endereco_data)
    assert EnderecoCliente.objects.filter(id=endereco.id).exists()
    assert endereco.rua == "Rua das Palmeiras"


@pytest.mark.django_db
def test_cadastrar_cliente_salva_no_banco():
    endereco = EnderecoCliente.objects.create(
        rua="Rua das Palmeiras",
        numero=123,
        complemento="Apto 101",
        bairro="Centro",
        cidade="São Paulo",
        estado="SP",
        cep="01000-000"
    )
    cliente_data = Cliente(
        nome="Josemar",
        cpf="12345678900",
        email="josemar@example.com",
        endereco=endereco,
        telefone="(11)91234-5678",
        data_nascimento="1990-01-01"
    )

    cadastrar_cliente(cliente_data)
    assert Cliente.objects.filter(nome="Josemar").exists()
