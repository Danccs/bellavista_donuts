from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import ProductoForm, IngredienteForm, ProveedorForm, ProductoIngredienteForm
from .models import Producto, Ingrediente, Proveedor, ProductoIngrediente

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
        form_producto_ingrediente = ProductoIngredienteForm(datos)

        if formcrear.is_valid() and form_producto_ingrediente.is_valid():
            producto = formcrear.save()
            ingrediente = form_producto_ingrediente.cleaned_data['ingrediente']

            ProductoIngrediente.objects.create(
                producto=producto,
                ingrediente=ingrediente,
                cantidad_ingrediente=form_producto_ingrediente.cleaned_data['cantidad_ingrediente']
            )


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

#Para proveedores
def v_mostrar_prov(request):
    context = {
        'proveedores': Proveedor.objects.all()

    }
    return render(request, 'mostrar_prov.html', context)

def v_crear_prov(request):
    if request.method == 'POST':
        datos = request.POST.copy()
        formcrear = ProveedorForm(datos)
        if formcrear.is_valid():
            formcrear.save()
            return HttpResponseRedirect(reverse('mostrar_prov'))

    context = {
        'formulario': ProveedorForm()
    }
    return render(request, 'crear_prov.html', context)

def v_editar_prov(request, proveedor_id):
    proveedor = Proveedor.objects.get(id = proveedor_id)

    if request.method == 'POST':
        datos = request.POST.copy()
        formeditar = ProveedorForm(datos, instance= proveedor)
        if formeditar.is_valid():
            formeditar.save()
            return render(request, 'editar_prov.html', {'formedicion': formeditar, 
                                                        'proveedor': proveedor})    
    else:
        context = {
            'formedicion': ProveedorForm(instance = proveedor)
        }
    return render(request, 'editar_prov.html', context)