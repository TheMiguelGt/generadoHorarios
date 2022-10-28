# Generated by Django 4.0.8 on 2022-10-28 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0008_history'),
        ('institucion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'dia',
            },
        ),
        migrations.CreateModel(
            name='Hora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iniHora', models.CharField(max_length=45)),
                ('finHora', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'hora',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=10)),
                ('materia', models.CharField(max_length=45, verbose_name='Nombre de la materia')),
                ('carga', models.IntegerField()),
            ],
            options={
                'db_table': 'materia',
            },
        ),
        migrations.CreateModel(
            name='DocenteMateria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institucion.aula')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.docente')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.page')),
            ],
            options={
                'db_table': 'docenteMateria',
            },
        ),
        migrations.CreateModel(
            name='disponibilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.dia')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.docente')),
                ('hora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.hora')),
            ],
            options={
                'db_table': 'disponibilidad',
            },
        ),
    ]
