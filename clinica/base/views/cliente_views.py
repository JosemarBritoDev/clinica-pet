from django.shortcuts import render, redirect
from clinica.base.decorators import cargo_requerido
from clinica.base.entidades import cliente, endereco
from clinica.base.forms.cliente_forms import ClienteForm
from clinica.base.forms.endereco_forms import EnderecoClienteForm
from clinica.base.services import cliente_service, endereco_service, pet_service, \
    consulta_service


# 🔒 Cargos permitidos: todos (0, 1, 2, 3)
@cargo_requerido([0, 1, 2, 3])
def listar_clientes(request):
    clientes = cliente_service.listar_clientes()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})


# 🔒 Cargos permitidos: todos (0, 1, 2, 3)
@cargo_requerido([0, 1, 2, 3])
def listar_cliente_id(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    pets = pet_service.listar_pets(id)
    consultas = consulta_service.listar_consultas_pets(id)
    return render(request, 'clientes/lista_cliente.html', {'cliente': cliente, 'pets': pets,
                                                           'consultas': consultas})


# 🔒 Cargos permitidos: Administrador (0), Recepcionista (2)
@cargo_requerido([0, 2])
def remover_cliente(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    endereco = endereco_service.listar_endereco_id(cliente.endereco.id)
    if request.method == 'POST':
        cliente_service.remover_cliente(cliente)
        endereco_service.remover_endereco(endereco)
        return redirect('base:listar_clientes')
    return render(request, 'clientes/confirma_exclusao.html', {'cliente': cliente})


# 🔒 Cargos permitidos: Administrador (0), Recepcionista (2)
@cargo_requerido([0, 2])
def cadastrar_cliente(request):
    if request.method == 'POST':
        form_cliente = ClienteForm(request.POST)
        form_endereco = EnderecoClienteForm(request.POST)

        if form_cliente.is_valid() and form_endereco.is_valid():
            endereco_novo = endereco.Endereco(
                rua=form_endereco.cleaned_data['rua'],
                numero=form_endereco.cleaned_data['numero'],
                complemento=form_endereco.cleaned_data['complemento'],
                bairro=form_endereco.cleaned_data['bairro'],
                cidade=form_endereco.cleaned_data['cidade'],
                estado=form_endereco.cleaned_data['estado'],
                cep=form_endereco.cleaned_data['cep'],
            )
            endereco_bd = endereco_service.cadastrar_endereco(endereco_novo)

            cliente_novo = cliente.Cliente(
                nome=form_cliente.cleaned_data['nome'],
                email=form_cliente.cleaned_data['email'],
                cpf=form_cliente.cleaned_data['cpf'],
                telefone=form_cliente.cleaned_data['telefone'],
                data_nascimento=form_cliente.cleaned_data['data_nascimento'],
                endereco=endereco_bd,
            )
            cliente_service.cadastrar_cliente(cliente_novo)
            clientes = cliente_service.listar_clientes()
            return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})
    else:
        form_cliente = ClienteForm()
        form_endereco = EnderecoClienteForm()

    return render(request, 'clientes/form_cliente.html', {
        'form_cliente': form_cliente,
        'form_endereco': form_endereco,
    })


# 🔒 Cargos permitidos: Administrador (0), Recepcionista (2)
@cargo_requerido([0, 2])
def editar_cliente(request, id):
    cliente_editar = cliente_service.listar_cliente_id(id)
    if hasattr(cliente_editar.data_nascimento, 'strftime'):
        cliente_editar.data_nascimento = cliente_editar.data_nascimento.strftime('%Y-%m-%d')

    form_cliente = ClienteForm(request.POST or None, instance=cliente_editar)
    endereco_editar = endereco_service.listar_endereco_id(cliente_editar.endereco.id)
    form_endereco = EnderecoClienteForm(request.POST or None, instance=endereco_editar)

    if form_cliente.is_valid():
        nome = form_cliente.cleaned_data['nome']
        email = form_cliente.cleaned_data['email']
        cpf = form_cliente.cleaned_data['cpf']
        telefone = form_cliente.cleaned_data['telefone']
        data_nascimento = form_cliente.cleaned_data['data_nascimento']

        if form_endereco.is_valid():
            endereco_novo = endereco.Endereco(
                rua=form_endereco.cleaned_data['rua'],
                numero=form_endereco.cleaned_data['numero'],
                complemento=form_endereco.cleaned_data['complemento'],
                bairro=form_endereco.cleaned_data['bairro'],
                cidade=form_endereco.cleaned_data['cidade'],
                estado=form_endereco.cleaned_data['estado'],
                cep=form_endereco.cleaned_data['cep'],
            )
            endereco_editado = endereco_service.editar_endereco(endereco_editar, endereco_novo)

            cliente_novo = cliente.Cliente(
                nome=nome,
                email=email,
                cpf=cpf,
                telefone=telefone,
                data_nascimento=data_nascimento,
                endereco=endereco_editado,
            )
            cliente_service.editar_cliente(cliente_editar, cliente_novo)
            return redirect('base:listar_clientes')

    return render(request, 'clientes/form_cliente.html', {
        'form_cliente': form_cliente,
        'form_endereco': form_endereco,
    })
