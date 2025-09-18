from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from functools import wraps


def cargo_requerido(cargos_permitidos, redirect_url='base:login'):
    """
    Decorator que exige que o usuário esteja autenticado e tenha um cargo permitido.
    Se não estiver logado ou não tiver permissão, será redirecionado para a URL definida.
    """
    def decorator(view_func):
        @login_required(login_url=redirect_url)
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if hasattr(request.user, 'cargo') and request.user.cargo in cargos_permitidos:
                return view_func(request, *args, **kwargs)
            return redirect(redirect_url)
        return _wrapped_view
    return decorator
