# Generated by Django 4.1.1 on 2022-09-10 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=60)),
                ('country', models.CharField(max_length=60)),
                ('zip_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]