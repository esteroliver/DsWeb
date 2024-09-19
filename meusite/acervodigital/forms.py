from django import forms

class CadastroForm(forms.Form):
    nome = forms.CharField(label='Nome:', max_length=100)
    nome_user = forms.CharField(label='Nome de usuário:', max_length=30)
    email = forms.EmailField(label='E-mail:')
    senha = forms.CharField(label='Senha:', max_length=50)

class LoginForm(forms.Form):
    nome_user = forms.CharField(label='Nome de usuário:', max_length=30)
    senha = forms.CharField(label='Senha:', max_length=50)

class AddLivroForm(forms.Form):
    titulo = forms.CharField(label='Título:', max_length=120)
    autor = forms.CharField(label='Autor:', max_length=120)
    ano = forms.CharField(label='Ano:', max_length=4)
    capa = forms.FileField(label='Capa:', required=False)

class AddContatoForm(forms.Form):
    nome = forms.CharField(label='Nome:', max_length=120)
    email = forms.EmailField(label='E-mail:')