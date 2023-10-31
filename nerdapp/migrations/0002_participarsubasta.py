# Generated by Django 4.2.5 on 2023-10-30 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nerdapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticiparSubasta',
            fields=[
                ('id_participacion', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.IntegerField()),
                ('id_subasta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nerdapp.subasta')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nerdapp.usuario')),
            ],
        ),
    ]