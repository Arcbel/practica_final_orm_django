from django.contrib import admin
from laboratorio.models import Laboratorio, DirectorGeneral, Producto

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_laboratorio')
    ordering = ('nombre_laboratorio',)

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_director_general', 'laboratorio')
    ordering = ('nombre_director_general',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_producto', 'laboratorio', 'año_fabricacion', 'p_costo', 'p_venta')
    ordering = ('nombre_producto', 'laboratorio')

    def año_fabricacion(self, obj):
        return obj.f_fabricacion.year
    año_fabricacion.short_description = 'f fabricacion'

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
