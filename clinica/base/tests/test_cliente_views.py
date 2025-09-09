import pytest
from django.urls import reverse
from unittest.mock import patch


@pytest.mark.django_db
def test_cadastrar_cliente_view(client):
    url = reverse('base:cadastrar_cliente')  # Certifique-se de que esse nome está no seu urls.py

    # Dados simulados do formulário
    cliente_data = {
        'nome': 'Josemar',
        'email': 'josemar@example.com',
        'cpf': '12345678900',
        'telefone': '(11)91234-5678',
        'data_nascimento': '1990-01-01',
        'rua': 'Rua das Palmeiras',
        'numero': 123,
        'complemento': 'Apto 101',
        'bairro': 'Centro',
        'cidade': 'São Paulo',
        'estado': 'SP',
        'cep': '01000-000'
    }

    with patch('clinica.base.services.endereco_service.cadastrar_endereco') as mock_endereco, \
         patch('clinica.base.services.cliente_service.cadastrar_cliente') as mock_cliente:

        mock_endereco.return_value = 'endereco_mockado'

        response = client.post(url, data=cliente_data)

        # Verifica se os serviços foram chamados
        mock_endereco.assert_called_once()
        mock_cliente.assert_called_once()

        # Verifica se a resposta foi um render da página (status 200)
        assert response.status_code == 200
        assert 'form_cliente' in response.context
        assert 'form_endereco' in response.context
