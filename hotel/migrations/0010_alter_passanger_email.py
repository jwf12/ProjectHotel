# Generated by Django 4.1.7 on 2023-03-13 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_remove_room_passanger_passanger_adress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passanger',
            name='email',
            field=models.CharField(blank=True, max_length=205, null=True),
        ),
    ]
