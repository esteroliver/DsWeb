from django.shortcuts import render
from django.http import HttpResponse
from .models import Pergunta

def index(request):
    lista_ult_perguntas = Pergunta.objects.all()
    contexto = {'lista': lista_ult_perguntas}
    return render(request, 'enquetes/index.html', contexto)

def detalhes(request, pergunta_id):
    resultado = "DETALHES da pergunta - %s"
    return HttpResponse(resultado % pergunta_id)

def votacao(request, pergunta_id):
    resultado = "VOTAÇÃO da pergunta - %s"
    return HttpResponse(resultado % pergunta_id)

def resultado(request, pergunta_id):
    resultado = "RESULTADO da pergunta - %s"
    return HttpResponse(resultado % pergunta_id)

