# Generated by Django 4.1.7 on 2023-04-01 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0018_alter_reservation_type_res'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='type_res',
            field=models.CharField(choices=[('1', 'Sgl'), ('2', 'Dbl'), ('3', 'Tpl'), ('4', 'Qdpl')], default='1', max_length=4),
        ),
    ]