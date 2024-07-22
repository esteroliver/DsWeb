import datetime
from django.db import models
from django.utils import timezone

class Pergunta(models.Model):
    texto = models.CharField(max_length=200)
    data_pub = models.DateTimeField('Data de publicação')
    def __str__(self):
        return '{} ({})'.format(self.texto, self.id)
    def publicada_recentemente(self):
        agora = timezone.now()
        return agora - datetime.timedelta(days=1) <= self.data_pub <= agora

class Alternativa(models.Model):
    texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    pergunta_ass = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    def __str__(self):
        return '{} ({})'.format(self.texto, self.id)

