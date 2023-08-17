from django.db import models

class Laboratorio (models.Model):
    nombre_laboratorio = models.CharField(max_length = 40)
    ciudad = models.CharField(max_length = 40, default = '')
    pais = models.CharField(max_length = 40, default = '')

    def __str__(self):
        return self.nombre_laboratorio

class DirectorGeneral(models.Model):
    nombre_director_general = models.CharField(max_length = 40)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.PROTECT)
    especialidad = models.CharField(max_length=40, default = '')

    def __str__(self):
        return self.nombre_director_general

class Producto (models.Model):
    nombre_producto = models.CharField(max_length = 40)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.PROTECT)
    f_fabricacion = models.DateField()
    p_costo = models.DecimalField(max_digits = 10, decimal_places = 2)
    p_venta = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return self.nombre_producto