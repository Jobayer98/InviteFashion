# Generated by Django 5.0.6 on 2024-06-01 03:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InviteFashionAPI', '0005_remove_productitem_quantity_in_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='porduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_items', to='InviteFashionAPI.product'),
        ),
    ]
