# Generated by Django 5.0.4 on 2024-04-16 16:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fin_app", "0014_alter_cryptomodel_crypto_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cryptomodel",
            name="crypto_id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
