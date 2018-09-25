from django.urls import path, include
from cotacao import views

urlpatterns = [
    path('', views.dados_pessoais, name= 'cotacao_dados_pessoais'),
]
