from django.urls import path
from . import views

urlpatterns = [
    path('', views.CadastroView.as_view(), name='cadastro'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('contatos/', views.ContatosView.as_view(), name='contatos'),
    path('emprestimos/', views.EmprestimosView.as_view(), name='emprestimos'),
    path('emprestimos/devolucao/', views.RegistrarDevolucaoView.as_view(), name='devolucao'),
    path('', views.PesquisarView.as_view(), name='pesquisar')
]