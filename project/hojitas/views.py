from django.shortcuts import render
from django.http import HttpResponse


def inicio(request): #request es la solicitud a la aplicación
    return render(request, 'paginas/inicio.html')


def nosotros(request):
    return render(request,'paginas/nosotros.html')


def hojas(request):
    return render(request, 'hojas/index.html')

def crearh(request):
    return render(request, 'hojas/crearh.html')

def editarh(request):
    return render(request, 'hojas/editarh.html')