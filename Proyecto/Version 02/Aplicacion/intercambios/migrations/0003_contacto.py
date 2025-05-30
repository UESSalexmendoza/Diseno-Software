# Generated by Django 5.2.1 on 2025-05-16 19:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intercambios', '0002_alter_usuario_contactoprincipal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('comentario', models.TextField(max_length=1000)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_envio', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
