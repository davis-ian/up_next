# Generated by Django 4.0.1 on 2022-01-23 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='release',
        ),
    ]
