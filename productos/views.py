from django.shortcuts import render
from .forms import ProductoForm
from .models import Producto

# Create your views here.
def v_mostrar_prod(request):
    context = {

    }
    return render(request, 'mostrar_prod.html', context)

def v_crear_prod(request):
    context = {
        'formulario': ProductoForm()
    }
    return render(request, 'crear_prod.html', context)

def v_editar_prod(request, producto_id):
    producto = Producto.objects.get(id = producto_id)

    if request.method == 'POST':
        pass
    else:
        context = {
            'formedicion': ProductoForm(instance = producto)
        }
    return render(request, 'editar_prod.html', context)