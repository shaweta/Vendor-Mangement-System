# Generated by Django 5.0.4 on 2024-05-02 08:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_alter_historicalperformance_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalperformance',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='items',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')], max_length=10),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor'),
        ),
    ]