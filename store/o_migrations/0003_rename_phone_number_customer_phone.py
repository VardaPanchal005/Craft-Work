# Generated by Django 4.1.4 on 2022-12-21 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_customer_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
