# Generated by Django 3.1.7 on 2021-04-20 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_remove_cartinfo_update_quantity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartInfo',
        ),
    ]
