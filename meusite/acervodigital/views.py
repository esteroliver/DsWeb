from django.shortcuts import render, redirect
from django.views import View
from .models import Livro, Usuario, Contato, Emprestimo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CadastroForm, LoginForm, AddLivroForm, AddContatoForm

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
        user = request.user.usuario
        livros_disponiveis = user.livro_set.filter(emprestado=False)
        livros_emprestados = user.livro_set.filter(emprestado=True)
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
                capa = capa,
                dono = request.user.usuario
            )
            livro.save()
        return redirect('/acervodigital/index')


class ContatosView(View):
    def get(self, request, *args, **kwargs):
        add_contato = AddContatoForm()
        user = request.user.usuario
        contatos = user.contato_set.all()
        contexto = {
            'contatos': contatos,
            'formulario': add_contato
            }
        return render(request, 'acervodigital/contatos.html', contexto)
    def post(self, request, *args, **kwargs):
        add_contato = AddContatoForm(request.POST)
        if add_contato.is_valid():
            nome = add_contato.cleaned_data['nome']
            email = add_contato.cleaned_data['email']

            contato = Contato.objects.create(
                nome = nome,
                email = email,
                usuario = request.user.usuario
            )
            contato.save()
        return redirect('/acervodigital/contatos')

class EmprestimosView(View):
    def get(self, request, *args, **kwargs):
        user = request.user.usuario
        livros = user.livro_set.filter(emprestado=False)
        contatos = user.contato_set.all()
        emprestimos = user.emprestimo_set.all()
        contexto = {
            'livros': livros,
            'contatos': contatos,
            'emprestimos': emprestimos
            }
        return render(request, 'acervodigital/emprestimos.html', contexto)
    def post(self, request, *args, **kwargs):
        usuario = request.user.usuario
        livro_id = request.POST.get('livro')
        contato_id = request.POST.get('contato')
        livro = Livro.objects.get(id=livro_id)
        contato = Contato.objects.get(id=contato_id)

        emprestimo = Emprestimo.objects.create(
            usuario = usuario,
            livro = livro,
            contato = contato
            )
        emprestimo.save()

        livro.emprestado = True
        livro.save()
        return redirect('/acervodigital/emprestimos')

class RegistrarDevolucaoView(View):
    def post(self, request, *args, **kwargs):
        emprestimo_id = request.POST.get('emprestimo')
        emprestimo = Emprestimo.objects.get(id=emprestimo_id)
        emprestimo.devolvido = True
        emprestimo.save()

        livro = Livro.objects.get(id=emprestimo.livro.id)
        livro.emprestado = False
        livro.save()

        return redirect('/acervodigital/emprestimos')

class PesquisarView(View):
    def get(self, request, *args, **kwargs):
        pesquisa = request.GET.get('search', '')
        livros = Livro.objects.filter(usuario=request.user, nome__icontains=pesquisa)
        contexto = {
            "livros": livros
            }
        return render(request, 'acervodigital/base.html')








