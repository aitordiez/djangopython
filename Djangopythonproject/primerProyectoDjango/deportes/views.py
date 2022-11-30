from django.shortcuts import render

# Create your views here.

def pedirDeportes(request):
    mensajes = {"titulo": "Futbol", "Descripcion": "El futbol es un deporte"}
    return render(request,'deportesFutbol.html',mensajes)

def listaDatosEquipo(request):
    listado_equipos_mundial = [
        {"seleccion": "España","numero_mundiales":"1","continente":"Europa"},
        {"seleccion": "Camerun", "numero_mundiales": "2","continente":"Africa"},
        {"seleccion": "EEUU", "numero_mundiales":"0","continente":"America"}

    ]
    contexto = {"listado_equipos":listado_equipos_mundial}
    return render(request,"equipos.html",contexto)