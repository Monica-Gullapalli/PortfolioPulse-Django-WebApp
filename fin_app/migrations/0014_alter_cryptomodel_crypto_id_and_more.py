# Generated by Django 5.0.4 on 2024-04-16 16:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fin_app", "0013_alter_cryptomodel_crypto_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cryptomodel",
            name="crypto_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="stockmodel",
            name="stock_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]