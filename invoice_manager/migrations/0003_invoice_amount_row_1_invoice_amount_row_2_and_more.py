# Generated by Django 4.1.1 on 2022-09-25 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_manager', '0002_alter_invoice_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='amount_row_1',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='amount_row_2',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='amount_row_3',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='amount_row_4',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='amount_row_5',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='item_name_row_1',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='item_name_row_2',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='item_name_row_3',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='item_name_row_4',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='item_name_row_5',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='item_num_row_1',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='item_num_row_2',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='item_num_row_3',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='item_num_row_4',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='item_num_row_5',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='po_num_row_1',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='po_num_row_2',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='po_num_row_3',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='po_num_row_4',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='po_num_row_5',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='price_ea_row_1',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='price_ea_row_2',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='price_ea_row_3',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='price_ea_row_4',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='price_ea_row_5',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='qty_ea_row_1',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='qty_ea_row_2',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='qty_ea_row_3',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='qty_ea_row_4',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AddField(
            model_name='invoice',
            name='qty_ea_row_5',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_po',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_customer_check_number',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.DecimalField(decimal_places=0, default='00000', max_digits=20),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_total',
            field=models.CharField(default='00000', max_length=60),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='item_quantity',
            field=models.DecimalField(decimal_places=4, default='00000', max_digits=20),
        ),
    ]
