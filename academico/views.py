from django.shortcuts import render, redirect
from datetime import datetime
from academico.models import *
from academico.forms import *

# Create your views here.

def carreras(request) :
    actual = datetime.now()
    mensaje = "CON DIOS, EN EL NOMBRE DE JESUS, TENDREMOS LA VICTORIA"
    rQ = request.GET.get('Q')
    if rQ is None:
        carreras = Carrera.objects.all() 
        context = {"actual":actual, "mensaje":mensaje, "carreras":carreras}
    else:
        carreras_list = Carrera.objects.filter(facultad__icontains = rQ)
        context = {"actual":actual, "mensaje":mensaje, "carreras":carreras_list}
    return render(request, "carreras.html", context)

def c_carreras(request) :
    if request.method == "POST" :
        form = CarreraForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect("carreras")
        else :
            message = "INFORMACION NO VALIDA, INTENTE DE NUEVO"
            return render(request, "create.html", {"message":message})
    else :
        form = CarreraForm()
        context = {'form':form}    
    return render(request, "create.html", context)

def u_carreras(request, pk) :
    i = Carrera.objects.get(id=pk)
    if request.method == "POST" :
        form = CarreraForm(request.POST, instance=i)
        if form.is_valid() :
            form.save()
            return redirect("carreras")
        else :
            message = "INFORMACION NO VALIDA, INTENTE DE NUEVO"
            return render(request, "create.html", {"message":message})
    else :
        form = CarreraForm(instance=i)
        context = {'form':form}    
    return render(request, "create.html", context)


def d_carreras(request, pk) :
    i = Carrera.objects.get(id=pk)
    i.delete()
    return redirect('carreras')