# Generated by Django 4.2.5 on 2023-10-25 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField()),
                ('precio', models.IntegerField(default=0)),
                ('cantidad_disponible', models.IntegerField(default=0)),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.AutoField(primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_rol', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subasta',
            fields=[
                ('id_subasta', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio_inicial', models.IntegerField()),
                ('precio_mas_alto', models.IntegerField()),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True)),
                ('fecha_termino', models.DateField()),
                ('hora_inicio', models.TimeField(auto_now_add=True)),
                ('hora_termino', models.TimeField()),
                ('imagen', models.ImageField(null=True, upload_to='subastas')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('apellido_paterno', models.CharField(max_length=200, null=True)),
                ('apellido_materno', models.CharField(max_length=200, null=True)),
                ('correo', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_subasta',
            fields=[
                ('id_usuario_subasta', models.AutoField(primary_key=True, serialize=False)),
                ('subasta_id_subasta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nerdapp.subasta')),
                ('usuario_id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nerdapp.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id_publicacion', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_publicacion', models.CharField(max_length=200)),
                ('descripcion_publicacion', models.IntegerField()),
                ('fecha_publicacion', models.DateField()),
                ('estado_publicacion', models.CharField(max_length=200)),
                ('usuario_id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nerdapp.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.AutoField(primary_key=True, serialize=False)),
                ('comuna', models.CharField(max_length=200)),
                ('region_id_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nerdapp.region')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id_comentario', models.AutoField(primary_key=True, serialize=False)),
                ('comentario', models.CharField(max_length=200)),
                ('fecha_comentario', models.DateField()),
                ('estado_comentario', models.CharField(max_length=200)),
                ('usuario_id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nerdapp.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id_carrito', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_compra', models.DateField()),
                ('total_venta', models.IntegerField()),
                ('iva', models.IntegerField()),
                ('usuario_id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nerdapp.usuario')),
            ],
        ),
    ]
