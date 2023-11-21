from django.shortcuts import render
from django.http import HttpResponse
# Estos elementos son esenciales para construir la interfaz de usuario y manejar las respuestas del servidor en una aplicación web Django.

# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo")

def formulario(request):
    return render(request, "formulario.html")
    # la función index devuelve un saludo simple "Hola Mundo" como respuesta HTTP, mientras que la función formulario utiliza la función render para renderizar una plantilla HTML llamada "formulario.html" como respuesta HTTP. 

def result(request):
    LITROS_MINUTO = 5
    totalGastado = 0
    calificacion = ''

    ducha = int(request.GET.get('ducha'))
    bano = int(request.GET.get('bano'))

    ducha = ducha * LITROS_MINUTO
    bano = bano * LITROS_MINUTO

    totalGastado = ducha + bano

    # realiza cálculos relacionados con el uso de agua basándose en los datos proporcionados en la solicitud GET. La función no retorna nada ni realiza ninguna acción adicional después de estos cálculos, por lo que su resultado (si lo hay) no se utiliza actualmente en el código proporcionado. 
    
    if totalGastado > 100:
        calificacion = 'Consumo excesivo'
    elif totalGastado == 100:
        calificacion = 'Consumo moderado'
    else:
        calificacion = 'Consumo bajo'


    return render(request, 'result.html', {'ducha': ducha, 
                                           'bano': bano,
                                           'totalGastado': totalGastado,
                                           'calificacion': calificacion})


# código evalúa el consumo total de agua (totalGastado) y establece una calificación en función de ese consumo. Luego, renderiza la plantilla 'result.html' junto con algunos datos adicionales como contexto, que probablemente se utilizarán para mostrar resultados y calificaciones en la interfaz de usuario.






