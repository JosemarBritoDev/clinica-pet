import pytest

@pytest.fixture
def cliente(client):
    """Alias em português para o fixture padrão do pytest-django `client`."""
    return client
