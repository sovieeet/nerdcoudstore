# Generated by Django 4.2.5 on 2023-10-22 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nerdapp', '0006_producto_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria_id_categoria',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='inventario_id_inventario',
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(),
        ),
    ]