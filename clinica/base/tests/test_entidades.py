
from clinica.base.entidades.endereco import Endereco
from clinica.base.entidades.cliente import Cliente


def test_endereco_criacao_e_acesso():
    endereco = Endereco(
        rua="Rua das Palmeiras",
        numero=123,
        complemento="Apto 101",
        bairro="Centro",
        cidade="São Paulo",
        estado="SP",
        cep="01000-000"
    )

    assert endereco.rua == "Rua das Palmeiras"
    assert endereco.numero == 123
    assert endereco.complemento == "Apto 101"
    assert endereco.bairro == "Centro"
    assert endereco.cidade == "São Paulo"
    assert endereco.estado == "SP"
    assert endereco.cep == "01000-000"


def test_endereco_setters():
    endereco = Endereco("A", 1, "", "B", "C", "SP", "00000-000")
    endereco.rua = "Nova Rua"
    endereco.numero = 999
    endereco.complemento = "Casa"
    endereco.bairro = "Novo Bairro"
    endereco.cidade = "Rio de Janeiro"
    endereco.estado = "RJ"
    endereco.cep = "22000-000"

    assert endereco.rua == "Nova Rua"
    assert endereco.numero == 999
    assert endereco.complemento == "Casa"
    assert endereco.bairro == "Novo Bairro"
    assert endereco.cidade == "Rio de Janeiro"
    assert endereco.estado == "RJ"
    assert endereco.cep == "22000-000"


def test_cliente_criacao_e_acesso():
    endereco = Endereco("Rua A", 10, "Casa", "Bairro B", "Cidade C", "SP", "01000-000")
    cliente = Cliente(
        nome="Josemar",
        email="josemar@example.com",
        cpf="12345678900",
        telefone="(11)91234-5678",
        data_nascimento="1990-01-01",
        endereco=endereco
    )

    assert cliente.nome == "Josemar"
    assert cliente.email == "josemar@example.com"
    assert cliente.cpf == "12345678900"
    assert cliente.telefone == "(11)91234-5678"
    assert cliente.data_nascimento == "1990-01-01"
    assert cliente.endereco.rua == "Rua A"


def test_cliente_setters():
    endereco = Endereco("Rua A", 10, "Casa", "Bairro B",
                        "Cidade C", "SP", "01000-000")
    cliente = Cliente("A", "a@a.com", "000", "000",
                      "2000-01-01", endereco)

    cliente.nome = "Maria"
    cliente.email = "maria@example.com"
    cliente.cpf = "98765432100"
    cliente.telefone = "(11)90000-0000"
    cliente.data_nascimento = "1985-05-05"

    assert cliente.nome == "Maria"
    assert cliente.email == "maria@example.com"
    assert cliente.cpf == "98765432100"
    assert cliente.telefone == "(11)90000-0000"
    assert cliente.data_nascimento == "1985-05-05"
