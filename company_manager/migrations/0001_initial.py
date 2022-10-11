# Generated by Django 4.1.1 on 2022-10-08 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=60)),
                ('country', models.CharField(max_length=60)),
                ('zip_code', models.CharField(max_length=10)),
                ('tel', models.CharField(max_length=20)),
            ],
        ),
    ]