from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('estoque.urls')),
    
    # HS-15: Adiciona as URLs de autenticação padrão do Django (/accounts/login, /accounts/logout, etc.)
    path('accounts/', include('django.contrib.auth.urls')), 
]
