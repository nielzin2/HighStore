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
    # <int:pk> captura o ID para exclusão
    path('excluir/<int:pk>/', views.excluir_item, name='excluir_item'), 
]
