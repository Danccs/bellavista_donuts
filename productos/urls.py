from django.urls import path

from .views import v_mostrar_prod, v_crear_prod, v_editar_prod

urlpatterns = [
    path('', v_mostrar_prod),
    path('crear_prod', v_crear_prod),
    path('editar_prod/<int:producto_id>/', v_editar_prod),
]