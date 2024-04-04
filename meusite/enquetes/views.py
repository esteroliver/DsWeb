from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Pergunta, Alternativa
from django.urls import reverse

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
    try:
        pergunta = Pergunta.objects.get(pk=pergunta_id)
    except Pergunta.DoesNotExist:
        raise Http404('Pergunta não existe.') #pegando a pergunta

    try:
        pergunta_selecionada = pergunta.alternativa_set.get(pk=request.POST['voto']) #pergunta_selecionada vai receber uma alternativa que foi enviada pelo método post

    except (KeyError, Alternativa.DoesNotExist): #caso haja um KeyError (não existe o id) ou a pergunta não exista, haverá essa exceção
        contexto = {'pergunta':pergunta,
        'error_message':"Selecione uma opção"}
        return render(request, 'enquetes/detalhes.html', contexto) #caso um usuário não selecione uma opção

    else: #caso não entre no except
        pergunta_selecionada.votos += 1
        pergunta_selecionada.save() #quando alteramos o estado de um objeto, temos que salvar
        return HttpResponseRedirect(reverse('enquetes:resultado', args=(pergunta_id,))) #redirecionando para outra view (resultado) com o parâmetro pergunta_id, que faz parte de uma coleção
                               #   '/enquetes/pergunta_id/resultado'
    #não é necessário passar o request por causa do protocolo Http

def resultado(request, pergunta_id):
    try:
        pergunta = Pergunta.objects.get(pk=pergunta_id)
    except Pergunta.DoesNotExist:
        raise Http404('Pergunta não existe.')
    return render(request, 'enquetes/resultado.html', {'pergunta':pergunta})
