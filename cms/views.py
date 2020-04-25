from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404

from .models import Contenido

@csrf_exempt
def get_content(request, llave):
    if request.method == "PUT":
        valor = request.body.decode('utf-8')
        try:
            #si ya existe esa llave la sustituyo por el nuevo valor
            recurso = Contenido.objects.get(clave=llave)
            recurso.valor = valor
        except Contenido.DoesNotExist:
            recurso = Contenido(clave=llave, valor=valor)
        recurso.save()

    elif request.method == "GET" or request.method == 'PUT':
        respuesta = get_object_or_404(Contenido, clave=llave)
        if name.endswith('.css'):
            content_type='text/css'
        else:
            content_type='text/html'
        return HttpResponse(respuesta.valor, content_type=content_type)
