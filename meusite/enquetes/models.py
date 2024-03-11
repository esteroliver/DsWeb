from django.db import models

class Pergunta(models.Model):
    texto = models.CharField(max_lenght=200)
    data_pub = models.DateTimeField('Data de publicação')

class Alternativa(models.Model):
    texto = models.CharField(max_lenght=200)
    votos = models.IntegerField(default=0)
    pergunta_ass = models.ForeignKey(Pergunta, on_delete=models.CASCADE)

