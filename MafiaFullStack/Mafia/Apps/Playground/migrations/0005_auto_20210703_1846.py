# Generated by Django 3.1.7 on 2021-07-03 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Playground', '0004_room_noofplayers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='noOfPlayers',
            field=models.IntegerField(default=1),
        ),
    ]
