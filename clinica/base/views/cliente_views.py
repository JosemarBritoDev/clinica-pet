from django.shortcuts import render

from clinica.base.entidades import cliente, endereco
from clinica.base.forms.cliente_forms import ClienteForm
from clinica.base.forms.endereco_forms import EnderecoClienteForm
from clinica.base.services import cliente_service, endereco_service


def cadastrar_cliente(request):
    if request.method == 'POST':
        form_cliente = ClienteForm(request.POST)
        form_endereco = EnderecoClienteForm(request.POST)
        if form_cliente.is_valid():
            nome = form_cliente.cleaned_data['nome']
            email = form_cliente.cleaned_data['email']
            cpf = form_cliente.cleaned_data['cpf']
            telefone = form_cliente.cleaned_data['telefone']
            data_nascimento = form_cliente.cleaned_data['data_nascimento']
            if form_endereco.is_valid():
                rua = form_endereco.cleaned_data['rua']
                numero = form_endereco.cleaned_data['numero']
                complemento = form_endereco.cleaned_data['complemento']
                bairro = form_endereco.cleaned_data['bairro']
                cidade = form_endereco.cleaned_data['cidade']
                estado = form_endereco.cleaned_data['estado']
                cep = form_endereco.cleaned_data['cep']
                endereco_novo = endereco.Endereco(rua=rua, numero=numero,
                                                  complemento=complemento,
                                                  bairro=bairro,
                                                  cidade=cidade, estado=estado, cep=cep)
                endereco_bd = endereco_service.cadastrar_endereco(endereco_novo)
                cliente_novo = cliente.Cliente(nome=nome, email=email, cpf=cpf,
                                               telefone=telefone,
                                               data_nascimento=data_nascimento,
                                               endereco=endereco_bd)
                cliente_service.cadastrar_cliente(cliente_novo)
    else:
        form_cliente = ClienteForm()
        form_endereco = EnderecoClienteForm()
    return render(request, 'clientes/form_cliente.html',
                  {'form_cliente': form_cliente, 'form_endereco': form_endereco})
