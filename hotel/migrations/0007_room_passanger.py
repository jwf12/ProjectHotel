# Generated by Django 4.1.7 on 2023-03-05 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_remove_room_passanger'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='passanger',
            field=models.CharField(blank=True, max_length=205, null=True),
        ),
    ]
