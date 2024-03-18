from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pergunta_id>/', views.detalhes, name='detalhes'),
    path('<int:pergunta_id>/votacao/', views.votacao, name='votação'),
    path('<int:pergunta_id>/resultado/', views.resultado, name='resultado'),
]