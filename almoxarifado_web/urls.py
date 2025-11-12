"""
Definições de URL para o projeto almoxarifado_web.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Rota para o painel de administração do Django
    path('admin/', admin.site.urls),
    
    # Rota principal: Quando o usuário acessa a raiz, ele é encaminhado para as URLs da app 'estoque'
    path('', include('estoque.urls')), 
]
