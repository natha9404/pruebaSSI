# Generated by Django 2.0.13 on 2019-04-11 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='numero_documento_identificacion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='sexo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='tipo_documento_identificacion',
        ),
    ]
