from django.db import models


class Telefone(models.Model):
    numero = models.CharField(max_length=11)
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.numero


class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Segurado(models.Model):
    cpf = models.CharField(max_length=14)
    telefones = models.ManyToManyField(Telefone, blank=True, null=True)
    emails = models.ManyToManyField(Email, blank=True, null=True)

    def __str__(self):
        return str(self.cpf) + " - " + str(self.seguradodados_set.last())


# demais informações do Segurado
class SeguradoDados(models.Model):
    nome = models.CharField(max_length=100)
    pessoa_fisica = models.BooleanField()
    cpf = models.ForeignKey(
        Segurado,
        on_delete=models.PROTECT,
        verbose_name="CPF"
    )
    sexo = models.CharField(max_length=1)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


# quem está utilizando a plataforma para fazer cotação
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    segurado = models.ForeignKey(
        Segurado,
        on_delete=models.CASCADE,
        blank=True, null=True
    )

    def __str__(self):
        return str(self.id) + " - " + self.nome


class Veiculo(models.Model):
    cotacao = models.OneToOneField(
        Segurado,
        verbose_name="id da cotacao",
        on_delete=models.PROTECT)
    chassi = models.CharField(max_length=17, blank=True, null=True)
    placa = models.CharField(max_length=7, blank=True, null=True)
    marca = models.CharField(max_length=20, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    ano_modelo = models.PositiveIntegerField()
    ano_fabricacao = models.PositiveIntegerField()
    zero_km = models.BooleanField()


    def __str__(self):
        return self.modelo
