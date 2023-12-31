# Generated by Django 3.2.23 on 2023-12-21 17:37

import airplanes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('uid', models.CharField(default=airplanes.models.gen_uuid, max_length=15, primary_key=True, serialize=False, unique=True)),
                ('id', models.PositiveIntegerField(default=1)),
                ('passenger', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
