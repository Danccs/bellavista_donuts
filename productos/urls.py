from django.urls import path

from .views import v_list, v_create, v_update

urlpatterns = [
    path('', v_list),
    path('create', v_create),
    path('update/<int:producto_id>/', v_update),
]