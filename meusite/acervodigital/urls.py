from django.urls import path
from . import views

urlpatterns = [
    path('', views.CadastroView.as_view(), name='cadastro'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('index/', views.IndexView.as_view(), name='index'),
]