# Generated by Django 4.1 on 2022-09-02 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idU', models.CharField(max_length=10, verbose_name='Id usuario')),
                ('idTy', models.IntegerField(verbose_name='Id tipo')),
                ('nom', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apePat', models.CharField(max_length=100, verbose_name='Apellido paterno')),
                ('apeMat', models.CharField(max_length=100, verbose_name='Apellido materno')),
                ('cPass', models.CharField(max_length=15, verbose_name='Password')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('image', models.ImageField(upload_to='usuarios', verbose_name='Avatar')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
                'ordering': ['created'],
            },
        ),
    ]
