# Generated by Django 4.2 on 2023-04-12 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuyerRegister_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=20)),
                ('Age', models.CharField(max_length=20)),
                ('DateOfBirth', models.CharField(max_length=20)),
                ('Country', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=20)),
                ('Username', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
    ]
