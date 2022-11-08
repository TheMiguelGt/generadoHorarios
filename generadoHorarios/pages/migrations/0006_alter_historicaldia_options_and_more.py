# Generated by Django 4.0.8 on 2022-11-08 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0007_alter_historicalaula_options_and_more'),
        ('usuarios', '0012_alter_historicalalumno_options_and_more'),
        ('pages', '0005_alter_historicaldia_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicaldia',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical dia', 'verbose_name_plural': 'historical dias'},
        ),
        migrations.AlterModelOptions(
            name='historicaldisponibilidad',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical disponibilidad', 'verbose_name_plural': 'historical disponibilidads'},
        ),
        migrations.AlterModelOptions(
            name='historicaldocentemateria',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical docente materia', 'verbose_name_plural': 'historical docente materias'},
        ),
        migrations.AlterModelOptions(
            name='historicalhora',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical hora', 'verbose_name_plural': 'historical horas'},
        ),
        migrations.AlterModelOptions(
            name='historicalpage',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical page', 'verbose_name_plural': 'historical pages'},
        ),
        migrations.AlterField(
            model_name='docentemateria',
            name='aula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auladoce', to='institucion.aula'),
        ),
        migrations.AlterField(
            model_name='docentemateria',
            name='docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docedoce', to='usuarios.docente'),
        ),
        migrations.AlterField(
            model_name='docentemateria',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matdoce', to='pages.page'),
        ),
        migrations.AlterField(
            model_name='historicaldia',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicaldisponibilidad',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicaldocentemateria',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalhora',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalpage',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]
