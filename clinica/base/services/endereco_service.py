from clinica.base.models import EnderecoCliente


def cadastrar_endereco(endereco):
    return EnderecoCliente.objects.create(rua=endereco.rua, numero=endereco.numero,
                                          complemento=endereco.complemento,
                                          bairro=endereco.bairro, cidade=endereco.cidade,
                                          estado=endereco.estado, cep=endereco.cep)


def listar_endereco_id(id):
    return EnderecoCliente.objects.get(id=id)
