# Generated by Django 3.1.7 on 2021-05-27 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Delivery', '0004_auto_20210508_2309'),
        ('Order', '0002_auto_20210527_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.ManyToManyField(related_name='orders', to='Delivery.Delivery'),
        ),
    ]
