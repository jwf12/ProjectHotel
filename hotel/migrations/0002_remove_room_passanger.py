# Generated by Django 4.1.7 on 2023-03-03 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='passanger',
        ),
    ]
