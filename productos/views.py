from django.shortcuts import render
from .forms import ProductoForm
from .models import Producto

# Create your views here.
def v_list(request):
    context = {

    }
    return render(request, 'list.html', context)

def v_create(request):
    context = {
        'formulario': ProductoForm()
    }
    return render(request, 'create.html', context)

def v_update(request, producto_id):
    producto = Producto.objects.get(id = producto_id)

    if request.method == 'POST':
        pass
    else:
        context = {
            'formedicion': ProductoForm(instance = producto)
        }
    return render(request, 'update.html', context)