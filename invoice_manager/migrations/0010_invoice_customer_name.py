# Generated by Django 4.1.1 on 2022-10-01 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_manager', '0009_rename_customer_pricing_id_row_1_invoice_customer_pricing_ea_row_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='customer_name',
            field=models.CharField(default='00000', max_length=60),
        ),
    ]