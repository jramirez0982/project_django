from django.shortcuts import render
from datetime import datetime

# Create your views here.

def carreras(request) :
    actual = datetime.now()
    mensaje = "CON DIOS, EN EL NOMBRE DE JESUS, TENDREMOS LA VICTORIA"
    # CONTEXT - CONTENIDO DINAMICO --> DICCIONARIO
    context = {"actual":actual, "mensaje":mensaje}
    return render(request, "carreras.html", context)

