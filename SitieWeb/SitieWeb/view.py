import datetime
from django.http import HttpResponse
from django.template import Template,Context
def saludo(request):

 nombre="Angel"
 now=datetime.datetime.now()

 doc_ex=open("C:/Users/sairaf/Desktop/web/WebDjangoNew/SitieWeb/SitieWeb/Plantillas/miplantilla.html")
 ptl=Template(doc_ex.read())
 doc_ex.close()
 ctx=Context({"nombre_persona":nombre,"momento_actual":now})
 documento=ptl.render(ctx)
 return HttpResponse(documento)

def calcularedad(request,year,edad):

 periodo=year-2019
 edadfutura=edad+periodo
 documento="<html><body><h2> En el año %s tendras %s años</h2></body></html>"%(year,edadfutura)
 return HttpResponse(documento)