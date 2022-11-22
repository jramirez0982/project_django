from django.shortcuts import render
from datetime import datetime
from academico.models import *
# Create your views here.

def carreras(request) :
    actual = datetime.now()
    mensaje = "CON DIOS, EN EL NOMBRE DE JESUS, TENDREMOS LA VICTORIA"
    carreras = Carrera.objects.all()   #TRAER TODOS LOS ELEMENTOS DE LA TABLA CARRERA RETORNA OBJETO QUERYSET (ITERABLE)
    rQ = request.GET.get('Q')
    carreras_filt = Carrera.objects.filter(facultad = rQ)
    # CONTEXT - CONTENIDO DINAMICO --> DICCIONARIO
    context = {"actual":actual, "mensaje":mensaje, "carreras":carreras, "carreras_filt":carreras_filt}
    return render(request, "carreras.html", context)

