def test_home_status_code(cliente):
    resposta = cliente.get('/')
    assert resposta.status_code == 200

