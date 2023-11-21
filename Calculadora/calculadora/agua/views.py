from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo")

def formulario(request):
    return render(request, "formulario.html")

def result(request):
    LITROS_MINUTO = 5
    totalGastado = 0
    calificacion = ''

    ducha = int(request.GET.get('ducha'))
    bano = int(request.GET.get('bano'))

    ducha = ducha * LITROS_MINUTO
    bano = bano * LITROS_MINUTO

    totalGastado = ducha + bano
    
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
