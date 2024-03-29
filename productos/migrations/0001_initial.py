# Generated by Django 4.0.5 on 2024-01-24 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('presentacion', models.CharField(max_length=128)),
                ('unidad_receta', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=128)),
                ('nombre', models.CharField(max_length=128)),
                ('elaboracion', models.TextField()),
                ('puntos_criticos', models.TextField()),
                ('insumos_herramientas', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('direccion', models.TextField()),
                ('telefono_ofi', models.CharField(max_length=20)),
                ('correo_ofi', models.EmailField(max_length=254)),
                ('horario_atencion', models.TextField()),
                ('nombre_contacto', models.CharField(max_length=128)),
                ('telefono_contacto', models.CharField(max_length=20)),
                ('correo_contacto', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ProveedorIngrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.ingrediente')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoIngrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_ingrediente', models.FloatField()),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.ingrediente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='ingredientes',
            field=models.ManyToManyField(through='productos.ProductoIngrediente', to='productos.ingrediente'),
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='proveedor',
            field=models.ManyToManyField(to='productos.proveedor'),
        ),
    ]
