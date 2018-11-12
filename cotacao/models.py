from django.db import models


class Telefone(models.Model):
    numero = models.CharField(max_length=11)

    def __str__(self):
        return self.numero


class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Segurado(models.Model):
    cpf = models.CharField(max_length=14)
    pessoa_fisica = models.BooleanField()
    telefones = models.ManyToManyField(Telefone, verbose_name="Telefone", blank=True)
    emails = models.ManyToManyField(Email, verbose_name="Email", blank=True)

    def __str__(self):
        return str(self.cpf)  # + " - " + str(self.seguradodados_set.last().nome)


# demais informações do Segurado
class SeguradoDados(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.ForeignKey(
        Segurado,
        on_delete=models.PROTECT,
        verbose_name="CPF",
        blank=True,
        null=True
    )
    genero = models.CharField(max_length=10)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome + " - " + str(self.cpf.cpf)


# quem está utilizando a plataforma para fazer cotação
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
    telefones = models.ManyToManyField(Telefone, verbose_name="Telefone", blank=True)
    emails = models.ManyToManyField(Email, verbose_name="Email", blank=True)
    segurado = models.ForeignKey(
        Segurado,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.id) + " - " + self.nome


class Seguro(models.Model):
    renovacao = models.BooleanField()
    inicio_vigencia = models.DateField()
    termino_vigencia = models.DateField()
    seguradora = models.CharField(max_length=50, blank=True, null=True)
    apolice = models.CharField(max_length=20, blank=True, null=True)
    bonus = models.PositiveIntegerField(blank=True, null=True)
    qnt_sinistro = models.PositiveIntegerField(verbose_name="Quantidade de Sinistro", blank=True, null=True)

    def __str__(self):
        try:
            a = self.veiculo
        except Exception as e:
            return "Nâo utilizado" + " - " + str(self.inicio_vigencia)
        else:
            return str(self.veiculo)


class Condutor(models.Model):
    relacao = models.CharField(max_length=15)
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
    estado_civil = models.CharField(max_length=15)
    residencia = models.CharField(max_length=30)
    profissao = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class QAR (models.Model):
    cep = models.CharField(max_length=8, verbose_name="CEP")
    garagem_residencia = models.CharField(max_length=50)
    garagem_trabalho = models.CharField(max_length=50)
    garagem_curso = models.CharField(max_length=50)
    utilizacao_veiculo = models.CharField(max_length=20)
    condutores_25anos = models.BooleanField()
    condutores_25anos_sexo = models.CharField(max_length=10)
    distancia_trabalho = models.PositiveIntegerField()
    km_mensal = models.PositiveIntegerField()
    vitima_roubo = models.BooleanField(verbose_name="Vitima de Roubo")

    def __str__(self):
        return str(self.veiculo_set)


class Veiculo(models.Model):
    segurado = models.ForeignKey(
        Segurado,
        verbose_name="id da cotacao",
        on_delete=models.PROTECT
    )
    seguro = models.OneToOneField(
        Seguro,
        on_delete=models.PROTECT
    )
    principal_condutor = models.OneToOneField(
        Condutor,
        on_delete=models.PROTECT,
        blank=True, null=True
    )
    qar = models.OneToOneField(
        QAR,
        on_delete=models.PROTECT,
        verbose_name="QAR",
        blank=True, null=True
    )
    chassi = models.CharField(max_length=17, blank=True, null=True)
    placa = models.CharField(max_length=7, blank=True, null=True)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=100)
    combustivel = models.CharField(max_length=20)
    ano_modelo = models.PositiveIntegerField()
    ano_fabricacao = models.PositiveIntegerField()
    zero_km = models.BooleanField()
    alienacao = models.BooleanField()
    chassi_remarcado = models.BooleanField()
    blindagem = models.BooleanField()
    tipo_veiculo = models.CharField(max_length=20)
    isencao_fiscal = models.CharField(max_length=20)
    cat_anti_furto = models.CharField(max_length=50, verbose_name="Categoria Anti-furto")
    marca_anti_furto = models.CharField(max_length=50)

    def __str__(self):
        return self.modelo
