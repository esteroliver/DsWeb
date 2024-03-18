from django.shortcuts import render
from django.http import HttpResponse
from .models import Pergunta

def index(request):
    lista_ult_perguntas = Pergunta.objects.all()[:10]
    output = '<br>'.join(p.texto for p in lista_ult_perguntas)
    return HttpResponse(output)

def detalhes(request, pergunta_id):
    resultado = "DETALHES da pergunta - %s"
    return HttpResponse(resultado % pergunta_id)

def votacao(request, pergunta_id):
    resultado = "VOTAÇÃO da pergunta - %s"
    return HttpResponse(resultado % pergunta_id)

def resultado(request, pergunta_id):
    resultado = "RESULTADO da pergunta - %s"
    return HttpResponse(resultado % pergunta_id)

