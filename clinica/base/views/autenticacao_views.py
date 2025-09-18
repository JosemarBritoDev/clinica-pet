from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import redirect, render


def login_usuario(request):
    if request.method == 'POST':
        form_login = AuthenticationForm(data=request.POST)
        if form_login.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('base:listar_clientes')
            else:
                messages.error(request, "As credenciais do usuário estão incorretas.")
                return redirect('base:login')
    else:
        form_login = AuthenticationForm()
    return render(request, 'autenticacao/login.html', {'form_login': form_login})


def deslogar_usuario(request):
    logout(request)
    return redirect('base:login')
