#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
import os
import sys
#Este fragmento generalmente se encuentra al principio de un script de Django y es utilizado para configurar el entorno antes de ejecutar comandos específicos de Django, como la creación de una nueva aplicación, aplicar migraciones, ejecutar el servidor de desarrollo

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calculadora.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    #configura el entorno de Django y luego ejecuta el comando de Django correspondiente a través de la línea de comandos. Este tipo de patrón es común en scripts de Django para la ejecución de comandos de gestión de Django desde la línea de comandos.


if __name__ == '__main__':
    main()
    #se ejecute solo cuando el script se ejecuta directamente y no cuando se importa como un módulo en otro script. Esto es útil para separar la lógica de ejecución principal del script de otras funciones y variables que podrían ser útiles si el script se utiliza como un módulo en otro programa.





