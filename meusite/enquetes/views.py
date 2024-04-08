from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Pergunta, Alternativa
from django.urls import reverse
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        lista = Pergunta.objects.all()
        return render(request, 'enquetes/index.html', {'lista':lista})

class DetalhesView(View):
    def get(self, request, *args, **kwargs):
        pergunta_id = args['pk']
        try:
            pergunta = Pergunta.objects.get(pk = pergunta_id)
        except Pergunta.DoesNotExist:
            raise Http404('Pergunta não existe.')
        return render(request, 'enquetes/detalhes.html', {'pergunta':pergunta})

    def post(self, request, *args, **kwargs):
        pergunta_id = args['pk']
        try:
            pergunta = Pergunta.objects.get(pk=pergunta_id)
        except Pergunta.DoesNotExist:
            raise Http404('Pergunta não existe.')
        try:
            pergunta_selecionada = pergunta.alternativa_set.get(pk=request.POST['voto'])
        except (KeyError, Alternativa.DoesNotExist):
            contexto = {'pergunta':pergunta,
            'error_message':"Selecione uma opção"}
            return render(request, 'enquetes/detalhes.html', contexto)
        else:
            pergunta_selecionada.votos += 1
            pergunta_selecionada.save()
            return HttpResponseRedirect(reverse('enquetes:resultado', args=(pergunta_id,)))

class ResultadoView(View):
    def get(self, request, *args, **kwargs):
        pergunta_id = args['pk']
        try:
            pergunta = Pergunta.objects.get(pk = pergunta_id)
        except Pergunta.DoesNotExist:
            raise Http404('Pergunta não existe.')
        return render(request, 'enquetes/detalhes.html', {'pergunta':pergunta})