from django import forms
from .models import Producto, Ingrediente, Proveedor, ProductoIngrediente

class ProductoIngredienteForm(forms.ModelForm):
    class Meta:
        model = ProductoIngrediente
        fields = ['ingrediente', 'cantidad_ingrediente']
class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        exclude = []

class ProductoForm(forms.ModelForm):
    producto_ingrediente = ProductoIngredienteForm()
    class Meta:
        model = Producto
        exclude = ['ingredientes',]

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        exclude = []