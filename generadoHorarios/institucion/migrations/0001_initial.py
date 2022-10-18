# Generated by Django 4.0.7 on 2022-10-06 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Licenciatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=10)),
                ('licenciatura', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'licenciatura',
            },
        ),
        migrations.CreateModel(
            name='Plantel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=10)),
                ('plantel', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'plantel',
            },
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semestre', models.CharField(max_length=1)),
                ('licenciatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institucion.licenciatura')),
            ],
            options={
                'db_table': 'semestre',
            },
        ),
        migrations.AddField(
            model_name='licenciatura',
            name='plantel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institucion.plantel'),
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=10)),
                ('piso', models.CharField(max_length=2)),
                ('plantel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institucion.plantel')),
            ],
            options={
                'db_table': 'aula',
            },
        ),
    ]