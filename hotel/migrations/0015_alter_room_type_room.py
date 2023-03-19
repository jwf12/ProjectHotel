# Generated by Django 4.1.7 on 2023-03-19 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0014_alter_room_type_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='type_room',
            field=models.CharField(choices=[('1', 'Sgl'), ('2', 'Dbl'), ('3', 'Tpl'), ('4', 'Qdpl')], default='1', max_length=4),
        ),
    ]