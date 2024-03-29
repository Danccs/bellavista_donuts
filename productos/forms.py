from django import forms
from .models import Producto, Ingrediente, Proveedor, ProductoIngrediente

class ProductoIngredienteForm(forms.ModelForm):
    class Meta:
        model = ProductoIngrediente
        fields = ['ingrediente', 'cantidad_ingrediente']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        exclude = []
class IngredienteForm(forms.ModelForm):
    proveedor = forms.ModelMultipleChoiceField(queryset=Proveedor.objects.all())
    class Meta:
        model = Ingrediente
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    producto_ingrediente = ProductoIngredienteForm()
    class Meta:
        model = Producto
        exclude = ['ingredientes',]

