from django.shortcuts import render
from django.views import View
from .models import Livro

class IndexView(View):
    def get(self, request, *args, **kwargs):
        livros_disponiveis = Livro.objects.filter(emprestado=False)
        livros_emprestados = Livro.objects.filter(emprestado=True)
        livros = {
            'livros_disponiveis': livros_disponiveis,
            'livros_emprestados': livros_emprestados
            }
        return render(request, 'acervodigital/index.html', livros)

