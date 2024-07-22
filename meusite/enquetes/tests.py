from django.test import TestCase
import datetime
from django.utils import timezone

from .models import Pergunta

class PerguntaModelTestes(TestCase):
    def test_publicado_recentemente(self):
        time = timezone.now() + datetime.timedelta(days=30)
        questao_futura = Pergunta(data_pub = time)
        self.assertIs(questao_futura.publicada_recentemente(), False)