# Generated by Django 5.0 on 2023-12-19 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendorapp', '0008_alter_vendor_vendor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
