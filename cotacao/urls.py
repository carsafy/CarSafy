from django.urls import path, include
from cotacao import views


urlpatterns = [
    path('', views.usuario, name='cotacao_usuario'),
]
