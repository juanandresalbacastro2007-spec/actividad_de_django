from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hoja
from .forms import HojaForm


def inicio(request): #request es la solicitud a la aplicación
    return render(request, 'paginas/inicio.html')


def nosotros(request):
    return render(request,'paginas/nosotros.html')


def hojas(request):
    hojas=Hoja.objects.all()
    return render(request, 'hojas/index.html',{'hojas':hojas})



def editarh(request,id): #se agrega el parametro que necesitamos.
    hoja=Hoja.objects.get(id=id) #para que muestre los datos
    formulario=HojaForm(request.POST or None, request.FILES or None,
    instance=hoja)
    if formulario.is_valid() and request.POST: #o request.POST
        formulario.save()
        return redirect('hojas')
    return render(request, 'hojas/editarh.html',{'formulario':formulario})


def crearh(request):
    formulario=HojaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('hojas')
    return render(request, 'hojas/crearh.html', {'formulario':formulario})

def eliminarh(request, id):
    hoja=Hoja.objects.get(id=id)
    hoja.delete()
    return redirect('hojas') 