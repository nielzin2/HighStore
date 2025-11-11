from django.urls import path
from . import views # Importa as views (funções de lógica) da aplicação atual

# Define o namespace da aplicação para evitar conflitos de nomes
app_name = 'estoque'

urlpatterns = [
    # path('', views.home, name='home'), # Exemplo de rota para uma homepage
    
    # Rota para a Listagem de Itens (F-03)
    # Quando a URL for a raiz da app (ex: /), chama a view 'lista_itens'
    path('', views.lista_itens, name='lista_itens'), 
]
