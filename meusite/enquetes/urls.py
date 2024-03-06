from django.urls import path
from . import views

urlpatterns = [
    path('enquetes/', views.index, name='index'),
    #enquetes - endereço (localhost:8000/enquetes)
    #views.index - função que vai ser ativada nesse endereço
]