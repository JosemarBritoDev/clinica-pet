from django.shortcuts import render
from clinica.base.entidades import cliente, endereco
from clinica.base.forms.cliente_forms import ClienteForm
from clinica.base.forms.endereco_forms import EnderecoClienteForm
from clinica.base.services import cliente_service, endereco_service


def listar_clientes(request):
    clientes = cliente_service.listar_clientes()
    return render(request, 'clientes/lista_clientes.html', {
        'clientes': clientes
    })


def cadastrar_cliente(request):
    if request.method == 'POST':
        form_cliente = ClienteForm(request.POST)
        form_endereco = EnderecoClienteForm(request.POST)

        if form_cliente.is_valid() and form_endereco.is_valid():

            # monta e salva o endereço

            novo_end = endereco.Endereco(
                rua=form_endereco.cleaned_data['rua'],
                numero=form_endereco.cleaned_data['numero'],
                complemento=form_endereco.cleaned_data['complemento'],
                bairro=form_endereco.cleaned_data['bairro'],
                cidade=form_endereco.cleaned_data['cidade'],
                estado=form_endereco.cleaned_data['estado'],
                cep=form_endereco.cleaned_data['cep'],
            )
            endereco_bd = endereco_service.cadastrar_endereco(novo_end)

            # monta e salva o cliente

            novo_cli = cliente.Cliente(
                nome=form_cliente.cleaned_data['nome'],
                email=form_cliente.cleaned_data['email'],
                cpf=form_cliente.cleaned_data['cpf'],
                telefone=form_cliente.cleaned_data['telefone'],
                data_nascimento=form_cliente.cleaned_data['data_nascimento'],
                endereco=endereco_bd,
            )
            cliente_service.cadastrar_cliente(novo_cli)

            # em vez de redirect, renderiza lista de clientes (status 200)

            clientes = cliente_service.listar_clientes()
            return render(request, 'clientes/lista_clientes.html', {
                'clientes': clientes
            })

    else:
        form_cliente = ClienteForm()
        form_endereco = EnderecoClienteForm()

    return render(request, 'clientes/form_cliente.html', {
        'form_cliente':  form_cliente,
        'form_endereco': form_endereco,
    })
