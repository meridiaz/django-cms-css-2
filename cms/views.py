from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404

from .models import Contenido


def index(request):
    content_list = Contenido.objects.all()
    context = {'content_list': content_list}
    return render(request, 'cms/index.html', context)

@csrf_exempt
def get_content(request, nombre):
    if request.method == "PUT":
        valor = request.body.decode('utf-8')
        try:
            #si ya existe esa llave la sustituyo por el nuevo valor
            recurso = Contenido.objects.get(clave=nombre)
            recurso.valor = valor
        except Contenido.DoesNotExist:
            recurso = Contenido(clave=nombre, valor=valor)
        recurso.save()

    if request.method == "GET" or request.method == 'PUT':
        recurso = get_object_or_404(Contenido, clave=nombre)
        if nombre.endswith('.css'):
            content_type='text/css'
        else:
            content_type='text/html'

        return render(request, 'cms/content.html', {'recurso': recurso})
        #return HttpResponse(recurso.valor, content_type=content_type)
