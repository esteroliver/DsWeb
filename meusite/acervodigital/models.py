from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Livro(models.Model):
    titulo = models.CharField(max_length=120)
    autor = models.CharField(max_length=120)
    ano = models.CharField(max_length=4)
    capa = models.ImageField(upload_to='capas/', blank=True, null=True)
    emprestado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo + '-' + self.autor

class Contato(models.Model):
    email = models.CharField(max_length=120)
    nome = models.CharField(max_length=120)

    def __str__(self):
        return self.nome + '(' + self.email + ')'

class Emprestimo(models.Model):
    livro = models.OneToOneField(Livro, on_delete=models.CASCADE)
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    devolvido = models.BooleanField(default=False)

