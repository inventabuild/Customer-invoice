# Generated by Django 4.1.1 on 2022-10-04 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_manager', '0005_alter_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
