# Generated by Django 2.1 on 2018-09-23 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Segurado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('emails', models.ManyToManyField(to='cotacao.Email')),
            ],
        ),
        migrations.CreateModel(
            name='SeguradoDados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cotacao.Segurado', verbose_name='CPF')),
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
                ('sexo', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chassi', models.CharField(blank=True, max_length=17, null=True)),
                ('placa', models.CharField(blank=True, max_length=7, null=True)),
                ('marca', models.CharField(blank=True, max_length=20, null=True)),
                ('modelo', models.CharField(blank=True, max_length=100, null=True)),
                ('ano_modelo', models.PositiveIntegerField()),
                ('ano_fabricacao', models.PositiveIntegerField()),
                ('cotacao', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cotacao.Segurado', verbose_name='id da cotacao')),
            ],
        ),
        migrations.AddField(
            model_name='segurado',
            name='telefones',
            field=models.ManyToManyField(to='cotacao.Telefone'),
        ),
    ]