from django.contrib import admin

# Register your models here.
from .models import Producto, Proveedor, Ingrediente, ProductoIngrediente, Tipo, Subtipo

class ProductoIngredienteInline(admin.TabularInline):
    model = ProductoIngrediente
    extra = 1
    autocomplete_fields = ['ingrediente', ]

class TipoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class SubtipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')

class ProductoAdmin(admin.ModelAdmin):
    inlines = [ProductoIngredienteInline, ]
    list_display = ('id', 'codigo', 'nombre', 'imagen')

class IngredienteAdmin(admin.ModelAdmin):
    inlines = (ProductoIngredienteInline,)
    search_fields = ('nombre'),
    list_display = ('id', 'nombre')

class ProductoIngredienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'ingrediente', 'cantidad_ingrediente')

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(ProductoIngrediente, ProductoIngredienteAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Subtipo, SubtipoAdmin)
