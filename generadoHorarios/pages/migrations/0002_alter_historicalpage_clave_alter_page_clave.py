# Generated by Django 4.0.8 on 2022-11-15 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpage',
            name='clave',
            field=models.CharField(db_index=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='page',
            name='clave',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
