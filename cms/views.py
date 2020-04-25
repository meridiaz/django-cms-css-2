from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404

from .models import Contenido


def index(request):
    content_list = Contenido.objects.all()
    context = {'content_list': content_list}
    return render(request, 'cms/index.html', context)


def get_contenido(request, nombre):
    valor = request.body.decode('utf-8')
    try:
        # si ya existe esa llave la sustituyo por el nuevo valor
        recurso = Contenido.objects.get(clave=nombre)
        recurso.valor = valor
    except Contenido.DoesNotExist:
        recurso = Contenido(clave=nombre, valor=valor)
    recurso.save()


@csrf_exempt
def get_content(request, nombre):
    if request.method == "PUT":
        get_contenido(request, nombre)

    if request.method == "GET" or request.method == 'PUT':
        recurso = get_object_or_404(Contenido, clave=nombre)

        return render(request, 'cms/content.html', {'recurso': recurso,
                                                    'doc_css': 'main.css'})


@csrf_exempt
def get_content_css(request, nombre):
    if request.method == "PUT":
        get_contenido(request, nombre)

    if request.method == "GET" or request.method == 'PUT':
        recurso = get_object_or_404(Contenido, clave=nombre)
        return HttpResponse(recurso.valor, content_type='text/css')


def index_css(request):
    content_list = Contenido.objects.filter(clave__endswith='.css')
    context = {'content_list': content_list}
    return render(request, 'cms/index.html', context)
