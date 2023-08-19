from django.urls import path 
from .views import v_index, v_info_labs, v_agregar, v_editar, v_eliminar

urlpatterns= [
    path ('', v_index),
    path('info_labs', v_info_labs),
    path('add', v_agregar),
    path('<int:laboratorio_id>/edit', v_editar),
    path('<int:laboratorio_id>/delete', v_eliminar)
]