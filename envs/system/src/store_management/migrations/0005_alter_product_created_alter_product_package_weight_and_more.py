# Generated by Django 5.1.2 on 2024-10-19 02:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_management', '0004_alter_product_created_alter_product_quantaty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 19, 5, 8, 46, 675148)),
        ),
        migrations.AlterField(
            model_name='product',
            name='package_weight',
            field=models.DecimalField(decimal_places=1, default=True, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantaty',
            field=models.DecimalField(decimal_places=1, default=True, max_digits=10),
        ),
    ]
