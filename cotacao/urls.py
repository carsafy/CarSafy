from django.urls import path, include
from cotacao import views


urlpatterns = [
    path('', views.dados_pessoais, name= 'cotacao_dados_pessoais'),
    path('dados_pessoais_novo', views.dados_pessoais_cadastro, name='cotacao_dados_pessoais_cadastro')
]
