# Generated by Django 4.1.1 on 2023-06-27 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_pusher_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='url',
        ),
    ]
