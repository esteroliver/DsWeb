from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Pergunta

def index(request):
    lista_ult_perguntas = Pergunta.objects.all()
    contexto = {'lista': lista_ult_perguntas}
    return render(request, 'enquetes/index.html', contexto)

def detalhes(request, pergunta_id):
    try:
        pergunta = Pergunta.objects.get(pk=pergunta_id)
    except Pergunta.DoesNotExist:
        raise Http404('Pergunta não existe.')
    return render(request, 'enquetes/detalhes.html', {'pergunta':pergunta})

def votacao(request, pergunta_id):
    resultado = "VOTAÇÃO da pergunta - %s"
    return HttpResponse(resultado % pergunta_id)

def resultado(request, pergunta_id):
    resultado = "RESULTADO da pergunta - %s"
    return HttpResponse(resultado % pergunta_id)

