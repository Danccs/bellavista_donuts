from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(max_length = 128)
    nombre = models.CharField(max_length = 128)
    elaboracion = models.TextField()
    puntos_criticos = models.TextField()
    insumos_herramientas = models.TextField(default='')
    
    def __str__(self):
        return self.nombre
    
    def obtener_ingredientes(self):
        # Utiliza la relación inversa con ProductoIngrediente para obtener los ingredientes asociados al producto
        ingredientes = ProductoIngrediente.objects.filter(producto=self)
        # Devuelve la lista de ingredientes asociados a este producto
        return [relacion.ingrediente for relacion in ingredientes]

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

    def __str__(self):
        return self.nombre

class ProductoIngrediente(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.PROTECT)
    unidad_ingrediente = models.CharField(max_length=128)
    cantidad_ingrediente = models.FloatField()

class ProveedorIngrediente(models.Model):
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)


