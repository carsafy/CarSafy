# Generated by Django 2.1 on 2018-10-21 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotacao', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='condutor',
            old_name='sexo',
            new_name='genero',
        ),
        migrations.RenameField(
            model_name='seguradodados',
            old_name='sexo',
            new_name='genero',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='sexo',
            new_name='genero',
        ),
    ]
