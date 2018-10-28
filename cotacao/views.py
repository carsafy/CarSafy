from django.shortcuts import render, redirect
from .models import Usuario, Telefone, Email


def usuario(request):
    return render(request, 'cotacao/dados_usuario.html')


def segurado(request):
    mensagem = {}
    telefone = {}
    email = {}
    usuario = {}

    if request.method == 'POST':
        # verificando se existe algum telefone ja cadastrado
        try:
            telefone['numero'] = str(request.POST.get('telefone'))
            Telefone.objects.get(numero=telefone['numero'])
        except Exception as e:
            mensagem['mensagem_telefone'] = str(e)

            # cadastrando o telefone caso seja a primeira vez
            try:
                Telefone.objects.create(**telefone)
            except Exception as e:
                mensagem['mensagem_telefone2'] = str(e)
            else:
                mensagem['mensagem_telefone2'] = "Cadastro Realizado"
        else:
            mensagem['mensagem_telefone'] = "Ja cadastrado"

        # verificando se tem algum email cadastrado
        try:
            email['email'] = request.POST.get('e-mail')
            Email.objects.get(email=email['email'])
        except Exception as e:
            mensagem['mensagem_email'] = str(e)

            # cadastrando caso seja o primeiro e-mail
            try:
                Email.objects.create(**email)
            except Exception as e:
                mensagem['mensagem_email2'] = str(e)
            else:
                mensagem['mensagem_email2'] = "Cadastro Realizado"
        else:
            mensagem['mensagem_email'] = "Ja cadastrado"

        # realizando o cadastro do Usuario
        try:
            usuario['nome'] = request.POST.get('nome')
            usuario['genero'] = request.POST.get('genero')
            novo_usuario = Usuario.objects.create(**usuario)
        except Exception as e:
            mensagem['mensagem_usuario'] = e
        else:
            mensagem['mensagem_usuario'] = "cadastro realizado com sucesso"

            # realizando o cadastro do email
            try:
                email = request.POST.get('e-mail')
                cadastro = Email.objects.get(email=email)
                novo_usuario.emails.add(cadastro)
            except Exception as e:
                mensagem['mensagem_email3'] = str(e)
            else:
                mensagem['mensagem_email3'] = "Cadastro do email no cliente realizado com sucesso"

            # realizando o cadastro do telefone
            try:
                telefone = request.POST.get('telefone')
                cadastro = Telefone.objects.get(numero=telefone)
                novo_usuario.telefones.add(cadastro)
            except Exception as e:
                mensagem['mensagem_telefone3'] = str(e)
            else:
                mensagem['mensagem_telefone3'] = "Cadastro do telefone no cliente realizado com sucesso"

        return render(request, 'cotacao/segurado.html', mensagem)

    else:
        return redirect('cotacao_usuario')
