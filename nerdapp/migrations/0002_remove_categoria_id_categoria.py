# Generated by Django 4.2.5 on 2023-10-01 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nerdapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='id_categoria',
        ),
    ]
