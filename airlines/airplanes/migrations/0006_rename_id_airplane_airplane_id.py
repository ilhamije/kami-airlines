# Generated by Django 3.2.23 on 2023-12-25 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airplanes', '0005_auto_20231222_0815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airplane',
            old_name='id',
            new_name='airplane_id',
        ),
    ]
