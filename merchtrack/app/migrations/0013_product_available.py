# Generated by Django 4.2.13 on 2024-05-28 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_product_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
