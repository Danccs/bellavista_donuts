# Generated by Django 5.0.1 on 2024-01-25 18:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("productos", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ProveedorIngrediente",
        ),
    ]
