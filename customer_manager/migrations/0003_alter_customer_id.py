# Generated by Django 4.1.1 on 2022-09-22 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_manager', '0002_customer_delete_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.DecimalField(decimal_places=0, max_digits=1000000000, primary_key=True, serialize=False),
        ),
    ]