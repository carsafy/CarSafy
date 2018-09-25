from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import DadosPessoaisForm

# Create your views here.

def dados_pessoais (request):
    form = DadosPessoaisForm()
    data = {'form': form}
    return render (request, 'cotacao/cotacao.html', data)


def dados_pessoais_cadastro (request):
    form = DadosPessoaisForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cotacao_dados_pessoais')