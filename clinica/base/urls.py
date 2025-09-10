from django.urls import path
from clinica.base.views import cliente_views

app_name = 'base'  # Isso define o namespace usado no reverse()

urlpatterns = [
    path('cadastrar_cliente/', cliente_views.cadastrar_cliente, name='cadastrar_cliente'),
    path('listar_clientes/', cliente_views.listar_clientes, name='listar_clientes'),
    path('lista_cliente/<int:id>', cliente_views.listar_cliente_id, name='listar_cliente_id'),
]
