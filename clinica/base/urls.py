from django.urls import path
from clinica.base.views import cliente_views

app_name = 'base'  # Isso define o namespace usado no reverse()

urlpatterns = [
    path('', cliente_views.cadastrar_cliente, name='home'),
    path('cadastrar_cliente/', cliente_views.cadastrar_cliente, name='cadastrar_cliente'),
]
