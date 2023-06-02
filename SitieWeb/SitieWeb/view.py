import datetime
from django.http import HttpResponse
from django.template import Template,Context

class Persona(object):
 def __init__(self,nombre,apellido):
  self.nombre=nombre
  self.apellido=apellido
def saludo(request):
 P2=Persona("julio","santos")

 now=datetime.datetime.now()

 doc_ex=open("C:/Users/sairaf/Desktop/web/WebDjangoNew/SitieWeb/SitieWeb/Plantillas/miplantilla.html")
 ptl=Template(doc_ex.read())
 doc_ex.close()
 ctx=Context({"nombre_persona":P2.nombre,"apellido_persona":P2.apellido,"momento_actual":now, "temas":["pantillas","metodos"]})
 documento=ptl.render(ctx)
 return HttpResponse(documento)

def calcularedad(request,year,edad):

 periodo=year-2019
 edadfutura=edad+periodo
 documento="<html><body><h2> En el año %s tendras %s años</h2></body></html>"%(year,edadfutura)
 return HttpResponse(documento)