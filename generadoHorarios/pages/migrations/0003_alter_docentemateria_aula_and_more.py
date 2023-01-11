# Generated by Django 4.0.8 on 2022-11-24 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0002_alter_aula_table_alter_licenciatura_table_and_more'),
        ('usuarios', '0001_initial'),
        ('pages', '0002_alter_dia_table_alter_disponibilidad_table_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docentemateria',
            name='aula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institucion.aula'),
        ),
        migrations.AlterField(
            model_name='docentemateria',
            name='docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.docente'),
        ),
        migrations.AlterField(
            model_name='docentemateria',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.page'),
        ),
    ]
