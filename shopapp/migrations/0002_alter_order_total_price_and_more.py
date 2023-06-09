# Generated by Django 4.1.4 on 2023-02-11 14:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_product_amount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='p_price',
            field=models.DecimalField(decimal_places=2, max_digits=20, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterUniqueTogether(
            name='orderproduct',
            unique_together={('product', 'order')},
        ),
    ]
