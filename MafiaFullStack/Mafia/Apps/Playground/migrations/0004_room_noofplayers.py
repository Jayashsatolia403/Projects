# Generated by Django 3.1.7 on 2021-07-03 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Playground', '0003_auto_20210628_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='noOfPlayers',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
