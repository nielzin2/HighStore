from django.urls import path
from . import views

app_name = 'estoque'

urlpatterns = [
    # Rota 1: Listagem de Itens (Index - CRUD R)
    path('', views.lista_itens, name='lista_itens'), 
    
    # Rota 2: Adicionar Novo Item (CRUD C)
    path('novo/', views.adicionar_item, name='adicionar_item'), 
]
