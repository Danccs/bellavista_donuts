from django.db import models

# Create your models here.

class Tipo(models.Model):
    nombre = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre

class Subtipo(models.Model):
    nombre = models.CharField(max_length=128)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
class Proveedor(models.Model):
    nombre = models.CharField(max_length=128)
    direccion = models.TextField()
    telefono_ofi = models.CharField(max_length=20)
    correo_ofi = models.EmailField()
    horario_atencion = models.TextField()
    nombre_contacto = models.CharField(max_length=128)
    telefono_contacto = models.CharField(max_length=20)
    correo_contacto = models.EmailField()

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=128)
    presentacion = models.CharField(max_length=128)
    unidad_receta = models.CharField(max_length=5)
    proveedor = models.ManyToManyField(Proveedor)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length = 128)
    nombre = models.CharField(max_length = 128)
    elaboracion = models.TextField()
    puntos_criticos = models.TextField()
    insumos_herramientas = models.TextField(default='')
    ingredientes = models.ManyToManyField(Ingrediente, through="ProductoIngrediente")
    imagen = models.ImageField(upload_to='up_images/', null=True, blank=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, default='')
    subtipo = models.ForeignKey(Subtipo, on_delete=models.PROTECT, default='')


    
    def __str__(self):
        return self.nombre
"""
    def obtener_ingredientes(self):
        # Utiliza la relación inversa con ProductoIngrediente para obtener los ingredientes asociados al producto
        ingredientes = ProductoIngrediente.objects.filter(producto=self)
        # Devuelve la lista de ingredientes asociados a este producto
        return [relacion.ingrediente for relacion in ingredientes]
"""


class ProductoIngrediente(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.PROTECT)
    cantidad_ingrediente = models.FloatField()

