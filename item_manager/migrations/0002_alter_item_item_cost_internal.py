# Generated by Django 4.1.1 on 2022-09-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_cost_internal',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
