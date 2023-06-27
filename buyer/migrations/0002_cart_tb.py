# Generated by Django 4.2 on 2023-04-17 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_product_tb'),
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShippingDate', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=20)),
                ('Quantity', models.IntegerField(max_length=20)),
                ('Total', models.IntegerField(max_length=20)),
                ('BuyerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.buyerregister_tb')),
                ('ProductId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.product_tb')),
            ],
        ),
    ]