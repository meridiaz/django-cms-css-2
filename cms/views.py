from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Contenido

@csrf_exempt
def get_content(request, llave):

        valor = request.body.decode('utf-8')
        try:
            #si ya existe esa llave la sustituyo por el nuevo valor
            respuesta = Contenido.objects.get(clave=llave)
            respuesta.valor = valor
            respuesta.save()
        except Contenido.DoesNotExist:
            if request.method == "PUT":
                c = Contenido(clave=llave, valor=valor)
                c.save()
                return HttpResponse('<h1>Valor añadidio con exito</h1>')
            elif request.method == "GET":
                respuesta = "No existe contenido para la clave: " +llave
                return HttpResponse(respuesta.valor)
