from django.urls import path, include
from cotacao import views


urlpatterns = [
    path('', views.usuario, name='cotacao_usuario'),
    # path('usuario-cadastro', views.usuario_cadastro, name='cotacao_usuario_cadastro'),

    path('dados-segurado/', views.segurado, name='cotacao_segurado'),
]
