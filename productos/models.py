from django.db import models

# Create your models here.
class Producto(models.Model):
    cod_prod = models.CharField(max_length = 128)
    nombre_prod = models.CharField(max_length = 128)
    elaboracion = models.TextField()
    puntos_criticos = models.TextField()
    estado = models.BooleanField(default=0)