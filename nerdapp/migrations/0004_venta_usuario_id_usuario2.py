# Generated by Django 4.2.5 on 2023-11-16 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nerdapp', '0003_producto_categoria_id_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='usuario_id_usuario2',
            field=models.ForeignKey(default=15, on_delete=django.db.models.deletion.CASCADE, to='nerdapp.usuario'),
            preserve_default=False,
        ),
    ]
