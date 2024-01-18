from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import ProductoForm, IngredienteForm
from .models import Producto, Ingrediente

# Create your views here.
def v_mostrar_prod(request):
    context = {
        'productos': Producto.objects.all()

    }
    return render(request, 'mostrar_prod.html', context)

def v_crear_prod(request):
    if request.method == 'POST':
        datos = request.POST.copy()
        formcrear = ProductoForm(datos)
        if formcrear.is_valid():
            formcrear.save()
            return HttpResponseRedirect("/")

    context = {
        'formulario': ProductoForm()
    }
    return render(request, 'crear_prod.html', context)

def v_editar_prod(request, producto_id):
    producto = Producto.objects.get(id = producto_id)

    if request.method == 'POST':
        datos = request.POST.copy()
        formeditar = ProductoForm(datos, instance= producto)
        if formeditar.is_valid():
            formeditar.save()
            return render(request, 'editar_prod.html', {'formedicion': formeditar, 
                                                        'producto': producto})    
    else:
        context = {
            'formedicion': ProductoForm(instance = producto)
        }
    return render(request, 'editar_prod.html', context)

#Para ingredientes:
def v_mostrar_ing(request):
    context = {
        'ingredientes': Ingrediente.objects.all()

    }
    return render(request, 'mostrar_ing.html', context)

def v_crear_ing(request):
    if request.method == 'POST':
        datos = request.POST.copy()
        formcrear = IngredienteForm(datos)
        if formcrear.is_valid():
            formcrear.save()
            return HttpResponseRedirect(reverse('mostrar_ing'))

    context = {
        'formulario': IngredienteForm()
    }
    return render(request, 'crear_ing.html', context)

def v_editar_ing(request, ingrediente_id):
    ingrediente = Ingrediente.objects.get(id = ingrediente_id)

    if request.method == 'POST':
        datos = request.POST.copy()
        formeditar = IngredienteForm(datos, instance= ingrediente)
        if formeditar.is_valid():
            formeditar.save()
            return render(request, 'editar_ing.html', {'formedicion': formeditar, 
                                                        'ingrediente': ingrediente})    
    else:
        context = {
            'formedicion': IngredienteForm(instance = ingrediente)
        }
    return render(request, 'editar_ing.html', context)