# Generated by Django 4.0.8 on 2022-11-02 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_history'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disponibilidad',
            name='dia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='pages.dia'),
        ),
        migrations.AlterField(
            model_name='disponibilidad',
            name='docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doces', to='usuarios.docente'),
        ),
        migrations.AlterField(
            model_name='disponibilidad',
            name='hora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hours', to='pages.hora'),
        ),
    ]
