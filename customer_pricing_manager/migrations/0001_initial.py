# Generated by Django 4.1.1 on 2022-09-14 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer_manager', '0002_customer_delete_company'),
        ('item_manager', '0003_alter_item_item_cost_internal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_pricing', models.CharField(max_length=60)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_manager.customer')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item_manager.item')),
            ],
        ),
    ]
