# Generated by Django 3.1.7 on 2021-05-27 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
        ('Seller', '0003_seller_is_admin_verified'),
        ('Delivery', '0004_auto_20210508_2309'),
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customers',
        ),
        migrations.RemoveField(
            model_name='order',
            name='sellers',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='Customer.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sellerOfProduct', to='Seller.seller'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.ManyToManyField(null=True, related_name='orders', to='Delivery.Delivery'),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]