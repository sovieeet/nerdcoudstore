# Generated by Django 4.2.5 on 2023-12-03 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nerdapp', '0006_remove_comuna_region_id_region_delete_rol_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Delivery',
        ),
    ]
