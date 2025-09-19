from ..models import Funcionario
from django.shortcuts import get_object_or_404


def listar_funcionarios():
    return Funcionario.objects.all()


def listar_funcionario_id(id):
    return get_object_or_404(Funcionario, id=id)


def cadastrar_funcionario(funcionario):
    Funcionario.objects.create(
        nome=funcionario.nome,
        nascimento=funcionario.nascimento,
        cargo=funcionario.cargo,
        username=funcionario.username,
        password=funcionario.password
    )
