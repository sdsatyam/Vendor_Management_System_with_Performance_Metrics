# Generated by Django 5.0 on 2023-12-19 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendorapp', '0005_rename_vendor_id_vendor_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='id',
            new_name='vendor_id',
        ),
    ]
