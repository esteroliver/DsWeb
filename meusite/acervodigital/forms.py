from django import forms

class CadastroForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    nome_user = forms.CharField(label='Nome de usuário', max_length=30)
    email = forms.EmailField(label='E-mail')
    senha = forms.CharField(label='Senha', max_length=50)