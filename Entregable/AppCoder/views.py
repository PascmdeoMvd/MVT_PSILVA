from re import template
from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template

from .models import familiar


def saludo(request):
    return HttpResponse("Hola como va todo?")

def diahoy(request):
    dia=datetime.now()
    texto = f"Hoy es:<br>{dia}"
    return HttpResponse(texto)

def saludanombre(request,nombre):
    texto = f"Mi nombre es {nombre}"
    return HttpResponse(texto)

def probandoTemplate(request, nombre):
    
    mihtml = open(r"C:/Users/ENVY/OneDrive/2022/Programación/Pyton/CoderHouse/Inicial/MVT_Pablo-Silva/Entregable/AppCoder/templates/templates1.html")
    plantilla = template(mihtml.read())
    mihtml.close()
    mi_Contexto = Context({"my_name": nombre})
    documento = plantilla.render(mi_Contexto)
    return HttpResponse(documento)

def familiares(request, nombre, apellido, fecha_nac):
    familiar.save()
    texto = f"Nombre {nombre}, apellido {apellido}, fecha de nacimiento {fecha_nac}"
    return HttpResponse(texto)

def mostrarfamiliar(request):
    familia= familiar.objects.all()
return render(request, "templates1.html", {"familia":familia})  

