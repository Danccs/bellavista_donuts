from django.urls import path

from .views import v_mostrar_prod, v_crear_prod, v_editar_prod
from .views import v_mostrar_ing, v_crear_ing, v_editar_ing
from .views import v_mostrar_prov, v_crear_prov, v_editar_prov


urlpatterns = [
    path('', v_mostrar_prod, name='mostrar_prod'),
    path('crear_prod', v_crear_prod, name='crear_prod'),
    path('editar_prod/<int:producto_id>/', v_editar_prod, name='editar_prod'),
    path('mostrar_ing', v_mostrar_ing, name='mostrar_ing'),
    path('crear_ing', v_crear_ing),
    path('editar_ing/<int:ingrediente_id>/', v_editar_ing),
    path('mostrar_prov', v_mostrar_prov, name='mostrar_prov'),
    path('crear_prov', v_crear_prov),
    path('editar_prov/<int:proveedor_id>/', v_editar_prov),
]