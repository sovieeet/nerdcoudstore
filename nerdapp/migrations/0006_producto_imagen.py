# Generated by Django 4.2.5 on 2023-10-22 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nerdapp', '0005_alter_usuario_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]