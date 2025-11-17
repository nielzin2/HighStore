from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('estoque.urls')),
    
    # HS-15: Adiciona as URLs de autenticação padrão do Django (/accounts/login, /accounts/logout, etc.)
    path('accounts/', include('django.contrib.auth.urls')), 
]

app_name = 'estoque'

urlpatterns = [
    path('', views.lista_itens, name='lista_itens'), 
    path('novo/', views.adicionar_item, name='adicionar_item'), 
    path('editar/<int:pk>/', views.editar_item, name='editar_item'),
    path('deletar/<int:pk>/', views.deletar_item, name='deletar_item'),
    path('alerta/', views.alerta_estoque, name='alerta_estoque'),
    
    # Rota 6: NOVO - Registrar Movimentação para um Item Específico (HS-14)
    path('movimentar/<int:pk>/', views.registrar_movimentacao, name='registrar_movimentacao'),
    
    # Rota 7: NOVO - Listar Histórico de Movimentações (HS-14)
    path('historico/', views.historico_movimentacoes, name='historico_movimentacoes'),
]
