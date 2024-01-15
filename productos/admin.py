from django.contrib import admin

# Register your models here.
from .models import Producto, Proveedor, Ingrediente, ProductoIngrediente, ProveedorIngrediente

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre')

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class ProductoIngredienteAdmin(admin.ModelAdmin):
    list_display = ('producto_codigo', 'producto_nombre', 'ingrediente')

    def producto_codigo(self, obj):
        return obj.producto.codigo

    def producto_nombre(self, obj):
        return obj.producto.nombre

class ProveedorIngredienteAdmin(admin.ModelAdmin):
    list_display = ('ingrediente', 'proveedor')

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(ProductoIngrediente, ProductoIngredienteAdmin)
admin.site.register(ProveedorIngrediente, ProveedorIngredienteAdmin)
