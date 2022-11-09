# Generated by Django 4.0.8 on 2022-11-08 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0006_alter_historicalaula_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalaula',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical aula', 'verbose_name_plural': 'historical aulas'},
        ),
        migrations.AlterModelOptions(
            name='historicallicenciatura',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical licenciatura', 'verbose_name_plural': 'historical licenciaturas'},
        ),
        migrations.AlterModelOptions(
            name='historicalplantel',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical plantel', 'verbose_name_plural': 'historical plantels'},
        ),
        migrations.AlterModelOptions(
            name='historicalsemestre',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical semestre', 'verbose_name_plural': 'historical semestres'},
        ),
        migrations.AlterField(
            model_name='historicalaula',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicallicenciatura',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalplantel',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalsemestre',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]