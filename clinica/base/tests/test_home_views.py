def test_home_status_code(cliente):
    resposta = cliente.get('/base/cadastrar_cliente/')
    assert resposta.status_code == 200
