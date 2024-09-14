from django.shortcuts import render, redirect
from django.views import View
from .models import Livro, Usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CadastroForm, LoginForm, AddLivroForm

class LoginView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        formulario = LoginForm()
        return render(request, 'acervodigital/login.html', {'formulario': formulario})

    def post(self, request, *args, **kwargs):
        formulario = LoginForm(request.POST)
        if(formulario.is_valid()):
            nome_user = request.POST.get('nome_user')
            senha = request.POST.get('senha')
            usuario = User.objects.get(username=nome_user)
            if usuario != 0:
                user = authenticate(request, username=nome_user, password=senha)
                login(request, user)
                return redirect('/acervodigital/index')
            else:
                messages.error(request, 'Usuario não existe')
        else:
            redirect('/acervodigital')

class CadastroView(View):
    def get(self, request, *args, **kwargs):
        formulario = CadastroForm()
        return render(request, 'acervodigital/cadastro.html', {'formulario': formulario})

    def post(self, request, *args, **kwargs):
        formulario = CadastroForm(request.POST)
        if(formulario.is_valid()):
            nome_user = request.POST['nome_user']
            email = request.POST['email']
            nome = request.POST['nome']
            senha = request.POST['senha']
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
                return redirect('/acervodigital/login')
        else:
            return redirect('/acervodigital')

class IndexView(View):
    def get(self, request, *args, **kwargs):
        add_livro = AddLivroForm()
        livros_disponiveis = Livro.objects.filter(emprestado=False)
        livros_emprestados = Livro.objects.filter(emprestado=True)
        contexto = {
            'livros_disponiveis': livros_disponiveis,
            'livros_emprestados': livros_emprestados,
            'formulario' : add_livro
            }
        return render(request, 'acervodigital/index.html', contexto)
    def post(self, request, *args, **kwargs):
        add_livro = AddLivroForm(request.POST, request.FILES)
        if add_livro.is_valid():
            titulo = add_livro.cleaned_data['titulo']
            autor = add_livro.cleaned_data['autor']
            ano = add_livro.cleaned_data['ano']
            capa = add_livro.cleaned_data['capa']

            livro = Livro.objects.create(
                titulo = titulo,
                autor = autor,
                ano = ano,
                capa = capa
            )
            livro.save()

            return redirect('/acervodigital/index')
        else:
            livros_disponiveis = Livro.objects.filter(emprestado=False)
            livros_emprestados = Livro.objects.filter(emprestado=True)
            contexto = {
                'livros_disponiveis': livros_disponiveis,
                'livros_emprestados': livros_emprestados,
                'formulario': add_livro
            }
            return render(request, 'acervodigital/index.html', contexto)



