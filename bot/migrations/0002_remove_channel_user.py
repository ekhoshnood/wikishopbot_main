# Generated by Django 3.0.3 on 2020-02-08 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='user',
        ),
    ]
