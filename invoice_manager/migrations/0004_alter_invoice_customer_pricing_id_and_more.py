# Generated by Django 4.1.1 on 2022-09-26 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_pricing_manager', '0002_alter_customer_pricing_id'),
        ('item_manager', '0005_alter_item_id'),
        ('invoice_manager', '0003_invoice_amount_row_1_invoice_amount_row_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='customer_pricing_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer_pricing_manager.customer_pricing'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='item_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='item_manager.item'),
        ),
    ]
