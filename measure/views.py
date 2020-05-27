from django.shortcuts import render, HttpResponse
import requests

# Create your views here.
def measure(request):
    return render(request, "measure/measure.html")

def measure(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        longitud = request.GET['longitud']
        latitud = request.GET['latitud']
        tipo_de_terreno = request.GET['tipo_de_terreno']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': '%', 'value': value,'longitud':longitud,'latitud':latitud,"tipo_de_terreno":tipo_de_terreno}
            #response = requests.post('http://127.0.0.1:8000/measure/', args)
            response = requests.post('http://pi1-eafit-lalzate.azurewebsites.net/measures/', args) 

            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    #response = requests.get('http://127.0.0.1:8000/measure/')
    response = requests.get('http://pi1-eafit-lalzate.azurewebsites.net/measures/')
    # Convierte la respuesta en JSON
    measures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/measure.html", {'measures': measures})