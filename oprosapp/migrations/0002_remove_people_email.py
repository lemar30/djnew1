# Generated by Django 3.0.2 on 2020-01-25 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oprosapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='email',
        ),
    ]
