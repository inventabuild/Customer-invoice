# Generated by Django 4.1.1 on 2022-09-11 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_manager', '0002_alter_item_item_cost_internal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_cost_internal',
            field=models.CharField(max_length=60),
        ),
    ]