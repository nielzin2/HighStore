from django.urls import path
from . import views

app_name = 'estoque'

urlpatterns = [
    # Rota 1: Listagem de Itens (Index - CRUD R)
    path('', views.lista_itens, name='lista_itens'), 
    
    # Rota 2: Adicionar Novo Item (CRUD C)
    path('novo/', views.adicionar_item, name='adicionar_item'), 
    
    # Rota 3: Editar Item Específico (CRUD U)
    path('editar/<int:pk>/', views.editar_item, name='editar_item'),
    
    # Rota 4: Excluir Item Específico (CRUD D)
    path('deletar/<int:pk>/', views.deletar_item, name='deletar_item'),
    
    # Rota 5: NOVO - Alerta de Estoque Mínimo (HS-12)
    path('alerta/', views.alerta_estoque, name='alerta_estoque'),
]
