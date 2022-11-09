# Generated by Django 4.0.8 on 2022-11-08 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0007_alter_historicalaula_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalaula',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical aula'},
        ),
        migrations.AlterModelOptions(
            name='historicallicenciatura',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical licenciatura'},
        ),
        migrations.AlterModelOptions(
            name='historicalplantel',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical plantel'},
        ),
        migrations.AlterModelOptions(
            name='historicalsemestre',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical semestre'},
        ),
        migrations.AlterField(
            model_name='historicalaula',
            name='history_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='historicallicenciatura',
            name='history_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='historicalplantel',
            name='history_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='historicalsemestre',
            name='history_date',
            field=models.DateTimeField(),
        ),
    ]