# Generated by Django 4.1.1 on 2022-10-01 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_manager', '0007_remove_invoice_customer_po_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='customer_pricing_id_row_1',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='customer_pricing_id_row_2',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='customer_pricing_id_row_3',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='customer_pricing_id_row_4',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='customer_pricing_id_row_5',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='item_id_row_1',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='item_id_row_2',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='item_id_row_3',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='item_id_row_4',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='item_id_row_5',
            field=models.CharField(default='00000', max_length=60),
        ),
    ]