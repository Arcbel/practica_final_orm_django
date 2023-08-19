from django.urls import path 
from .views import v_index, v_info_labs, v_agregar

urlpatterns= [
    path ('', v_index),
    path('info_labs', v_info_labs),
    path('add', v_agregar),
]