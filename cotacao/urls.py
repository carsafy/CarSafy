from django.urls import path, include
from cotacao import views


urlpatterns = [
    path('', views.usuario, name='cotacao_usuario'),
    path('segurado/', views.segurado, name='cotacao_segurado'),
    path('veiculo/', views.veiculo, name='cotacao_veiculo'),
]
