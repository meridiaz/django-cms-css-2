from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Contenido

@csrf_exempt
def get_content(request, llave):
    if request.method == "PUT":
        valor = request.body.decode('utf-8')
        try:
            respuesta = Contenido.objects.get(clave=llave).valor
            #si ya existe esa llave la sustituyo por el nuevo valor
            valor2 = Contenido.objects.get(clave=llave)
            valor2.valor = valor
            valor2.save()
        except Contenido.DoesNotExist:
            c = Contenido(clave=llave, valor=valor)
            c.save()
        return HttpResponse('<h1>Valor añadidio con exito</h1>')

    elif request.method == "GET":
        try:
            respuesta = Contenido.objects.get(clave=llave).valor
        except Contenido.DoesNotExist:
            respuesta = "No existe contenido para la clave: " +llave
        return HttpResponse(respuesta)

@csrf_exempt
def get_content_css(request, recurso):
    #if request.method == "PUT":
        cuerpo = request.body.decode('utf-8')
        try:
            #si ya existe esa llave la sustituyo por el nuevo valor
            respuesta = Contenido.objects.get(clave=llave)
            respuesta.valor = cuerpo
            respuesta.save()
        except Contenido.DoesNotExist:
            c = Contenido(clave=recurso, valor=cuerpo)
            c.save()
        return HttpResponse('<h1>Valor añadidio con exito</h1>')
    #elif request.method == "GET":
