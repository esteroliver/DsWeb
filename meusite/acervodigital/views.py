from django.shortcuts import render, redirect
from django.views import View
from .models import Livro, Usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CadastroForm

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acervodigital/login.html')

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = User.objects.get(email=email)
        if user != 0:
            user = authenticate(request, username=user.username, password=senha)
            login(request, user)
            return redirect('/index')
        else:
            messages.error(request, 'Usuario não existe')

class CadastroView(View):
    def get(self, request, *args, **kwargs):
        formulario = CadastroForm()
        return render(request, 'acervodigital/cadastro.html', {'formulario': formulario})

    def post(self, request, *args, **kwargs):
        formulario = CadastroForm(request.POST)
        if(formulario.is_valid()):
            if User.objects.filter(username=nome_user).exists():
                messages.error("Já existe um usuário com esse username")
            elif User.objects.filter(email=email).exists():
                messages.error("Já existe um usuário com esse email")
            else:
                user = User.objects.create_user(
                    username = nome_user,
                    email = email,
                    first_name = nome,
                    password = senha
                )
                user.save()
                usuario = Usuario.objects.create(
                    user = user
                )
                usuario.save()
                return redirect('/login')
        else:
            return redirect('/')

class IndexView(View):
    def get(self, request, *args, **kwargs):
        livros_disponiveis = Livro.objects.filter(emprestado=False)
        livros_emprestados = Livro.objects.filter(emprestado=True)
        livros = {
            'livros_disponiveis': livros_disponiveis,
            'livros_emprestados': livros_emprestados
            }
        return render(request, 'acervodigital/index.html', livros)

