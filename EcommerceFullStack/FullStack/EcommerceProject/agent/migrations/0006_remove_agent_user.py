# Generated by Django 3.1.7 on 2021-04-26 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0005_agent_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='user',
        ),
    ]
