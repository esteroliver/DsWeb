from django.urls import path
from . import views

app_name = 'enquetes'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('<int:pk>/', views.DetalhesView, name='detalhes'),
    path('<int:pk>/resultado/', views.ResultadoView, name='resultado'),
]