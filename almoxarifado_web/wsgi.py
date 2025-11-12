"""
WSGI config for almoxarifado_web project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

# Define o módulo de configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'almoxarifado_web.settings')

application = get_wsgi_application()
