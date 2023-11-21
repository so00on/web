from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario', views.formulario, name='formulario'),
    path('result', views.result, name='result')
]

# indican cómo deben interpretarse y manejar las solicitudes HTTP entrantes en tu aplicación Django. Cuando un usuario accede a una URL específica, Django utiliza estas definiciones de ruta para dirigir la solicitud a la función de vista correspondiente, que procesará la solicitud y devolverá una respuesta. El uso de nombres (name) permite referenciar estas rutas de manera más fácil en otras partes del código, como en las plantillas HTML o en el propio código Python.






