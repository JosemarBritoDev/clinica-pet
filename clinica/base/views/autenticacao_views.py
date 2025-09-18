from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import redirect, render


# 🔐 View de login com redirecionamento por cargo
def login_usuario(request):
    if request.method == 'POST':
        form_login = AuthenticationForm(data=request.POST)
        if form_login.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)

                # Redireciona conforme o cargo
                if usuario.cargo == 0:  # Administrador
                    return redirect('base:listar_funcionarios')
                elif usuario.cargo == 1:  # Veterinário
                    return redirect('base:listar_clientes')
                elif usuario.cargo == 2:  # Recepcionista
                    return redirect('base:listar_clientes')
                elif usuario.cargo == 3:  # Auxiliar
                    return redirect('base:listar_clientes')
                else:
                    messages.warning(request, "Cargo não reconhecido. Redirecionado para clientes.")
                    return redirect('base:listar_clientes')
            else:
                messages.error(request, "As credenciais do usuário estão incorretas.")
                return redirect('base:login')
    else:
        form_login = AuthenticationForm()
    return render(request, 'autenticacao/login.html', {'form_login': form_login})


# 🔐 View de logout
def deslogar_usuario(request):
    logout(request)
    return redirect('base:login')
