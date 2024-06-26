# Generated by Django 5.0.4 on 2024-05-04 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0003_alter_historicalperformance_vendor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalperformance',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historical_performances', to='vendors.vendor'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='issue_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_orders', to='vendors.vendor'),
        ),
    ]
