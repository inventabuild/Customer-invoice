# Generated by Django 4.1.1 on 2022-10-02 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_manager', '0010_invoice_customer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='id',
            field=models.DecimalField(decimal_places=0, max_digits=1000000000, primary_key=True, serialize=False),
        ),
    ]
