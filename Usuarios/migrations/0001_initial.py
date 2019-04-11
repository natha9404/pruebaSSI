# Generated by Django 2.0.13 on 2019-04-10 21:12

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('tipo_documento_identificacion', models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('CE', 'Cédula de Extranjería')], max_length=20, verbose_name='tipo de identificación')),
                ('numero_documento_identificacion', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Solamente valores númericos')], verbose_name='número de documento')),
                ('telefono', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Solamente valores númericos')], verbose_name='Télefono')),
                ('sexo', models.CharField(blank=True, choices=[('MASCULINO', 'Masculino'), ('FEMENINO', 'Femenino')], max_length=20, null=True, verbose_name='Sexo')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
