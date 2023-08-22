from django.test import TestCase
from .models import Laboratorio

class LaboratorioTests(TestCase):
    def setUp(self):
        lab1 = Laboratorio()
        lab1.nombre_laboratorio= 'Labo 1'
        lab1.ciudad = 'Santiago'
        lab1.pais = 'Chile'
        lab1.save()

        lab2 = Laboratorio()
        lab2.nombre_laboratorio = 'Labo 2'
        lab2.ciudad = 'Bio Bio'
        lab2.pais = 'Chile'
        lab2.save()

        lab3 = Laboratorio()
        lab3.nombre_laboratorio = 'Labo 3'
        lab3.ciudad = 'Calama'
        lab3.pais = 'Chile'
        lab3.save()

    def test_info_labs(self):
        respuesta = self.client.get('/info_labs')
        labs = respuesta.context['laboratorios']
        self.assertEqual(3, labs.count())

    def test_visitas(self):
        respuesta = self.client.get('/info_labs')
        numv = respuesta.context['numveces']
        self.assertEqual(1, numv)

    def test_add(self):
        respuesta = self.client.post('/add', {
            'nombre_laboratorio': 'Lab 4',
            'ciudad': 'Iquique',
            'pais': 'Chile'
        }, follow = True)

        self.assertEqual(200, respuesta.status_code)
        self.assertTemplateUsed(respuesta, 'informacion_labs.html')

        self.assertEqual(4, Laboratorio.objects.all().count())



        
