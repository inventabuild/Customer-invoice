# Generated by Django 4.1.1 on 2022-09-19 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_manager', '0003_alter_item_item_cost_internal'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='number',
            field=models.CharField(max_length=60),
            preserve_default=False,
        ),
    ]