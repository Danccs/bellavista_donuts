from django import forms
from .models import Producto, Ingrediente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = []

class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        exclude = []