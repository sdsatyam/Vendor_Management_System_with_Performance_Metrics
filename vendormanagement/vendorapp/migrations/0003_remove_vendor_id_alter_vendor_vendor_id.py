# Generated by Django 5.0 on 2023-12-19 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendorapp', '0002_vendor_vendor_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='id',
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
