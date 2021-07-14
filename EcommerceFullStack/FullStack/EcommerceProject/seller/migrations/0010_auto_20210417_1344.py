# Generated by Django 3.1.7 on 2021-04-17 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0002_auto_20210417_1335'),
        ('seller', '0009_seller_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='agent',
            field=models.ManyToManyField(null=True, related_name='agent', to='agent.Agent'),
        ),
    ]