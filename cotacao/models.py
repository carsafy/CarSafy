from django.db import models

class DadosPessoais(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__ (self):
        return self.nome

