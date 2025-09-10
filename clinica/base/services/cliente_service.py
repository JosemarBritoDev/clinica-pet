from clinica.base.models import Cliente
from clinica.base.entidades.cliente import Cliente as ClienteEntidade  # se estiver usando DTOs


def cadastrar_cliente(cliente: ClienteEntidade) -> Cliente:
    """
    Recebe um objeto de entidade Cliente (DTO) e salva no banco como modelo Django.
    Retorna o objeto Cliente salvo.
    """
    cliente_model = Cliente.objects.create(
        nome=cliente.nome,
        email=cliente.email,
        endereco=cliente.endereco,
        cpf=cliente.cpf,
        data_nascimento=cliente.data_nascimento,
        telefone=cliente.telefone
    )
    return cliente_model


def listar_clientes() -> list[Cliente]:
    """
    Retorna todos os clientes cadastrados no banco.
    """
    return Cliente.objects.all()


def listar_cliente_id(id):
    return Cliente.objects.get(id=id)
