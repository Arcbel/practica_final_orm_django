from django.contrib import admin
from laboratorio.models import Laboratorio, DirectorGeneral, Producto

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_laboratorio')

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_director_general', 'laboratorio')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_producto', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
