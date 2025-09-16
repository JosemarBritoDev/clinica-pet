from django.urls import path
from clinica.base.views import cliente_views, pet_views, consulta_views

app_name = 'base'  # Namespace usado nas URLs para reverses como 'base:rota'

# Mapeamento de URLs para views da aplicação base.
# Cada path define uma rota, a view correspondente e um nome para uso em templates (tag url) e reverses.
urlpatterns = [
    # Clientes

    # Formulário de criação de cliente
    path('cadastrar_cliente/', cliente_views.cadastrar_cliente, name='cadastrar_cliente'),
    # Lista todos os clientes
    path('listar_clientes/', cliente_views.listar_clientes, name='listar_clientes'),
    # Perfil de um cliente específico
    path('lista_cliente/<int:id>', cliente_views.listar_cliente_id, name='listar_cliente_id'),
    # Edição de cliente
    path('editar_cliente/<int:id>', cliente_views.editar_cliente, name='editar_cliente'),
    # Exclusão de cliente
    path('remover_cliente/<int:id>', cliente_views.remover_cliente, name='remover_cliente'),

    # Pets

    # Cadastro de pet vinculado ao cliente (id do cliente)
    path('cadastrar_pet/<int:id>', pet_views.inserir_pet, name='cadastrar_pet'),
    # Exibe detalhes do pet e histórico
    path('listar_pet/<int:id>', pet_views.listar_pet_id, name='listar_pet_id'),

    # Consultas

    # Cadastro de consulta (id do pet)
    path('cadastrar_consulta/<int:id>', consulta_views.inserir_consulta, name='cadastrar_consulta'),
    # Visualiza uma consulta específica
    path('lista_consulta/<int:id>', consulta_views.listar_consulta_id, name='listar_consulta_id'),

]
