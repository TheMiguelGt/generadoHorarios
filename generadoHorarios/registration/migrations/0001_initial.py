# Generated by Django 4.0.7 on 2022-10-02 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import registration.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('C', 'ADMIN'), ('D', 'DOCENTE'), ('E', 'ESTUDIANTE')], default='E', max_length=15)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=registration.models.custom_upload_to)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
    ]
