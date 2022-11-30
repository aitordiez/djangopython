from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
'''
def bienvenido(request):
    return  HttpResponse("Hola mundo!")
'''

'''
def bienvenido(request):
    return render(request, "bienvenido.html")
'''

'''
def despedida(request):
    return render(request,"despedida.html")
'''


'''
def bienvenido(request):
    mensajes = {'mensaje1': "valor del mensaje 1","mensaje2":"valor del mensaje 2"}
    return render(request, "bienvenido.html",mensajes)
'''



def listaDatos(request):
    listado_alumnos = [
        {"nombre":"nombre1","apellidos":"Apellidos1","Dni":"1111A"},
        {"nombre": "nombre2", "apellidos": "Apellidos2", "Dni": "2222A"},
        {"nombre": "nombre3", "apellidos": "Apellidos3", "Dni": "3333A"}

    ]
    contexto = { "lsitado_alumnos":listado_alumnos}
    return render(request,"gestion/Alumnos.html",contexto)