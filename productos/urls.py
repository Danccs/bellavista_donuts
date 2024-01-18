from django.urls import path

from .views import v_mostrar_prod, v_crear_prod, v_editar_prod
from .views import v_mostrar_ing, v_crear_ing, v_editar_ing


urlpatterns = [
    path('', v_mostrar_prod),
    path('crear_prod', v_crear_prod),
    path('editar_prod/<int:producto_id>/', v_editar_prod),
    path('mostrar_ing', v_mostrar_ing, name='mostrar_ing'),
    path('crear_ing', v_crear_ing),
    path('editar_ing/<int:ingrediente_id>/', v_editar_ing),
]