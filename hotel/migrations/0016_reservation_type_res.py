# Generated by Django 4.1.7 on 2023-03-19 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0015_alter_room_type_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='type_res',
            field=models.CharField(choices=[('1', 'Sgl'), ('2', 'Dbl'), ('3', 'Tpl'), ('4', 'Qdpl')], default='1', max_length=4),
        ),
    ]