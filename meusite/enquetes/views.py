from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Pergunta

def index(request):
    lista_ult_perguntas = Pergunta.objects.all()
    template = loader.get_template('enquetes/index.html')
    contexto = {'lista': lista_ult_perguntas}
    return HttpResponse(template.render(contexto, request))

def detalhes(request, pergunta_id):
    resultado = "DETALHES da pergunta - %s"
    return HttpResponse(resultado % pergunta_id)

def votacao(request, pergunta_id):
    resultado = "VOTAÇÃO da pergunta - %s"
    return HttpResponse(resultado % pergunta_id)

def resultado(request, pergunta_id):
    resultado = "RESULTADO da pergunta - %s"
    return HttpResponse(resultado % pergunta_id)

