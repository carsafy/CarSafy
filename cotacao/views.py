from django.shortcuts import render, redirect
from .models import (
    Usuario,
    Telefone,
    Email,
    Segurado,
    SeguradoDados
)

def usuario(request):
    return render(request, 'cotacao/usuario.html')


def segurado(request):
    if request.method == 'POST':
        mensagem = {}
        telefone = {}
        email = {}
        usuario = {}

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

            request.session['usuario_id'] = novo_usuario.id  # armazenando o id do usuário
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


def veiculo(request):
    if request.method == 'POST':
        mensagem = {}
        usuario_id = request.session.get('usuario_id')

        # verificação se o CPF já foi cadastrado
        try:
            Segurado.objects.get(cpf=request.POST.get('cpf'))

        except Exception as e:
            mensagem['cpf'] = str(e)
            segurado_dados = {}
            segurado = {}

            # verificando se Segurado == usuário
            if request.POST.get('segurado') == 'sim':
                usuario = Usuario.objects.get(id=usuario_id)  # recuperando informações do usuario

                segurado_dados['nome'] = usuario.nome
                segurado_dados['genero'] = usuario.genero
            else:
                segurado_dados['nome'] = request.POST.get('nome')
                segurado_dados['genero'] = request.POST.get('genero')

            segurado_dados['data_nascimento'] = request.POST.get()

            novo_segurado_dados = SeguradoDados.objects.create(**segurado_dados)

            segurado['cpf'] = request.POST.get('cpf')

            if segurado['cpf'].__len__() == 11:
                segurado['pessoa_fisica'] = True
            else:
                segurado['pessoa_fisica'] = False

            novo_segurado = Segurado.objects.create(**segurado)



        return render(request, 'cotacao/veiculo.html')

    return redirect('cotacao_usuario')
