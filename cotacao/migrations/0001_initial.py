# Generated by Django 2.1 on 2018-10-21 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relacao', models.CharField(max_length=15)),
                ('cpf', models.CharField(max_length=11)),
                ('nome', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=10)),
                ('estado_civil', models.CharField(max_length=15)),
                ('residencia', models.CharField(max_length=30)),
                ('profissao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='QAR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8, verbose_name='CEP')),
                ('garagem_residencia', models.CharField(max_length=50)),
                ('garagem_trabalho', models.CharField(max_length=50)),
                ('garagem_curso', models.CharField(max_length=50)),
                ('utilizacao_veiculo', models.CharField(max_length=20)),
                ('condutores_25anos', models.BooleanField()),
                ('condutores_25anos_sexo', models.CharField(max_length=10)),
                ('distancia_trabalho', models.PositiveIntegerField()),
                ('km_mensal', models.PositiveIntegerField()),
                ('vitima_roubo', models.BooleanField(verbose_name='Vitima de Roubo')),
            ],
        ),
        migrations.CreateModel(
            name='Segurado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14)),
                ('pessoa_fisica', models.BooleanField()),
                ('emails', models.ManyToManyField(blank=True, to='cotacao.Email', verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='SeguradoDados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=10)),
                ('data_nascimento', models.DateField()),
                ('cpf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cotacao.Segurado', verbose_name='CPF')),
            ],
        ),
        migrations.CreateModel(
            name='Seguro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('renovacao', models.BooleanField()),
                ('inicio_vigencia', models.DateField()),
                ('termino_vigencia', models.DateField()),
                ('seguradora', models.CharField(blank=True, max_length=50, null=True)),
                ('apolice', models.CharField(blank=True, max_length=20, null=True)),
                ('bonus', models.PositiveIntegerField(blank=True, null=True)),
                ('qnt_sinistro', models.PositiveIntegerField(blank=True, null=True, verbose_name='Quantidade de Sinistro')),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=10)),
                ('emails', models.ManyToManyField(blank=True, to='cotacao.Email', verbose_name='Email')),
                ('segurado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cotacao.Segurado')),
                ('telefones', models.ManyToManyField(blank=True, to='cotacao.Telefone', verbose_name='Telefone')),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chassi', models.CharField(blank=True, max_length=17, null=True)),
                ('placa', models.CharField(blank=True, max_length=7, null=True)),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=100)),
                ('combustivel', models.CharField(max_length=20)),
                ('ano_modelo', models.PositiveIntegerField()),
                ('ano_fabricacao', models.PositiveIntegerField()),
                ('zero_km', models.BooleanField()),
                ('alienacao', models.BooleanField()),
                ('chassi_remarcado', models.BooleanField()),
                ('blindagem', models.BooleanField()),
                ('tipo_veiculo', models.CharField(max_length=20)),
                ('isencao_fiscal', models.CharField(max_length=20)),
                ('cat_anti_furto', models.CharField(max_length=50, verbose_name='Categoria Anti-furto')),
                ('marca_anti_furto', models.CharField(max_length=50)),
                ('principal_condutor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cotacao.Condutor')),
                ('qar', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cotacao.QAR', verbose_name='QAR')),
                ('segurado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cotacao.Segurado', verbose_name='id da cotacao')),
                ('seguro', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cotacao.Seguro')),
            ],
        ),
        migrations.AddField(
            model_name='segurado',
            name='telefones',
            field=models.ManyToManyField(blank=True, to='cotacao.Telefone', verbose_name='Telefone'),
        ),
    ]
