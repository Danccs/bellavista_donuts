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
        datos.update(request.FILES)  # para la carga de imagen
        formcrear = ProductoForm(datos)
        form_producto_ingrediente = ProductoIngredienteForm(datos)

        if formcrear.is_valid() and form_producto_ingrediente.is_valid():
            # no guardar aún, hay que agregar la imagen
            producto = formcrear.save(commit=False)
            producto.imagen = request.FILES.get('imagen')
            producto.save()
            ingrediente = form_producto_ingrediente.cleaned_data['ingrediente']

            ProductoIngrediente.objects.create(
                producto=producto,
                ingrediente=ingrediente,
                cantidad_ingrediente=form_producto_ingrediente.cleaned_data['cantidad_ingrediente']
            )

            if "agregar_otro" in request.POST:
                return HttpResponseRedirect(reverse("crear_prod"))

            return HttpResponseRedirect("/")
        
        else:
            print("¡Formularios no válidos!")
            print("Errores en ProductoForm:", formcrear.errors)
            print("Errores en ProductoIngredienteForm:", form_producto_ingrediente.errors)

    context = {
        'formulario': ProductoForm()
    }
    return render(request, 'crear_prod.html', context)


def v_editar_prod(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    ingredientes_asociados = ProductoIngrediente.objects.filter(
        producto=producto)
    todos_los_ingredientes = Ingrediente.objects.all()

    if request.method == 'POST':
        formeditar = ProductoForm(
            request.POST, request.FILES, instance=producto)
        if formeditar.is_valid():
            formeditar.save()

            for ingrediente_asociado in ingredientes_asociados:
                cantidad_key = f'cantidad_{ingrediente_asociado.id}'
                unidad_key = f'unidad_{ingrediente_asociado.id}'
                ingrediente_id = request.POST.get(
                    f'ingrediente_{ingrediente_asociado.id}')

                # Verifica si el ingrediente ha cambiado
                if str(ingrediente_asociado.ingrediente.id) != ingrediente_id:
                    nuevo_ingrediente = Ingrediente.objects.get(
                        id=ingrediente_id)
                    ingrediente_asociado.ingrediente = nuevo_ingrediente

                # Actualiza la cantidad
                ingrediente_asociado.cantidad_ingrediente = request.POST.get(
                    cantidad_key)

                # Actualiza la unidad de receta
                nueva_unidad = request.POST.get(unidad_key)
                if nueva_unidad:
                    ingrediente_asociado.ingrediente.unidad_receta = nueva_unidad
                
                ingrediente_asociado.save()

            # Construir una lista de tuplas que contienen el ingrediente, cantidad y unidad asociada
            ingredientes_con_cantidad_unidad = [
                (pi.ingrediente, pi.cantidad_ingrediente, pi.ingrediente.unidad_receta) for pi in ingredientes_asociados]

            #Verificando si la unidad de la receta se está pasando correctamente
            #print(ingredientes_con_cantidad_unidad)

            return render(request, 'editar_prod.html', {'formedicion': formeditar,
                                                        'producto': producto,
                                                        'ingredientes_asociados': ingredientes_asociados,
                                                        'todos_los_ingredientes': todos_los_ingredientes,
                                                        'ingredientes_con_cantidad_unidad': ingredientes_con_cantidad_unidad})
    else:
        formeditar = ProductoForm(instance=producto)
        context = {
            'formedicion': formeditar,
            'ingredientes_asociados': ingredientes_asociados,
            'todos_los_ingredientes': todos_los_ingredientes,
        }

    return render(request, 'editar_prod.html', context)

# Para ingredientes:


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
            ingrediente = formcrear.save(commit=False)

            # obteniendo el proveedor seleccionado desde el formulario
            proveedor_id = datos['proveedor']
            proveedor = Proveedor.objects.get(pk=proveedor_id)

            ingrediente.save()

            # asignando el proveedor usando el método set(), por django
            ingrediente.proveedor.set([proveedor])

            return HttpResponseRedirect(reverse('mostrar_ing'))

    context = {
        'formulario': IngredienteForm()
    }
    return render(request, 'crear_ing.html', context)


def v_editar_ing(request, ingrediente_id):
    ingrediente = Ingrediente.objects.get(id=ingrediente_id)

    if request.method == 'POST':
        formeditar = IngredienteForm(request.POST, instance=ingrediente)
        if formeditar.is_valid():
            formeditar.save()
            return render(request, 'editar_ing.html', {'formedicion': formeditar,})
    else:
        formeditar = IngredienteForm(instance=ingrediente)
        context = {
            'formedicion': formeditar,
        }

    return render(request, 'editar_ing.html', context)



# Para proveedores
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
    proveedor = Proveedor.objects.get(id=proveedor_id)

    if request.method == 'POST':
        datos = request.POST.copy()
        formeditar = ProveedorForm(datos, instance=proveedor)
        if formeditar.is_valid():
            formeditar.save()
            return render(request, 'editar_prov.html', {'formedicion': formeditar,
                                                        'proveedor': proveedor})
    else:
        context = {
            'formedicion': ProveedorForm(instance=proveedor)
        }
    return render(request, 'editar_prov.html', context)
