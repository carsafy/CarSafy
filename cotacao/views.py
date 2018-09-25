from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import DadosPessoaisForm

# Create your views here.

def dados_pessoais (request):
    form = DadosPessoaisForm()
    data = {'form': form}
    return render (request, 'cotacao/cotacao.html', data)

