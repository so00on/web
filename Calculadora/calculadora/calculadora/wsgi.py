"""
WSGI config for calculadora project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calculadora.settings')

application = get_wsgi_application()



#onfigura el entorno de Django y obtiene la aplicación WSGI para el proyecto, preparando así el proyecto Django para ser desplegado en un servidor web compatible con WSGI. 