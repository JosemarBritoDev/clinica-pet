import pytest
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()


@pytest.mark.django_db
def test_home_status_code(client):
    user = User.objects.create_user(
        username='teste',
        password='123456',
        cargo=0,
        nascimento=date(1990, 1, 1)
    )
    client.force_login(user)

    response = client.get('/base/cadastrar_cliente/')
    assert response.status_code == 200
