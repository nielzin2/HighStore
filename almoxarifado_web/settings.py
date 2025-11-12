"""
Configurações do Django para o projeto almoxarifado_web.
"""
import os
from pathlib import Path

# Definição do diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent


# --- Configurações de Segurança e Ambiente ---

# Chave SECRETA: Use para desenvolvimento.
SECRET_KEY = 'django-insecure-chave-de-teste-aqui' 

# CORRIGIDO: Necessário para rodar o servidor localmente.
DEBUG = True 

# CORRIGIDO: Permitir acesso de hosts locais.
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# --- Definição das Aplicações (Apps) ---

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Nossa aplicação de estoque
    'estoque', 
]

# Middlewares, Roots, Templates (Configurações Padrão)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'almoxarifado_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Diretório global de templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'almoxarifado_web.wsgi.application'


# CORRIGIDO: Configuração correta do Banco de Dados SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'almoxarifado.db', 
    }
}


# --- Configurações de Senhas e Internacionalização ---

AUTH_PASSWORD_VALIDATORS = [
    # ... (Default Validators)
]


# Internacionalização
LANGUAGE_CODE = 'pt-br' 
TIME_ZONE = 'America/Sao_Paulo' 
USE_I18N = True
USE_TZ = True


# --- Configurações de Arquivos Estáticos ---

STATIC_URL = '/static/'

# Padrão para a Primary Key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
