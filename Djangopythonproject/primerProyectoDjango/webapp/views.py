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



def bienvenido(request):
    mensajes = {'mensaje1': "valor del mensaje 1","mensaje2":"valor del mensaje 2"}
    return render(request, "bienvenido.html",mensajes)