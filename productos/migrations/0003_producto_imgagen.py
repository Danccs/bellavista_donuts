# Generated by Django 5.0.1 on 2024-01-28 23:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("productos", "0002_delete_proveedoringrediente"),
    ]

    operations = [
        migrations.AddField(
            model_name="producto",
            name="imgagen",
            field=models.ImageField(blank=True, null=True, upload_to="up_images/"),
        ),
    ]