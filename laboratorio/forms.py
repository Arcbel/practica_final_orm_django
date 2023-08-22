from django import forms
from .models import Laboratorio

class LaboratorioForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(LaboratorioForm, self).__init__(*args, **kwargs)
        self.fields['nombre_laboratorio'].widget.attrs['placeholder'] = 'Ingrese nombre del Laboratorio'
        self.fields['ciudad'].widget.attrs['placeholder'] = 'Ingrese ciudad del Laboratorio'
        self.fields['pais'].widget.attrs['placeholder'] = 'Ingrese país del Laboratorio'

    class Meta:
        model = Laboratorio
        exclude = []
        #fields = ['nombre_laboratorio', 'ciudad', 'pais'] 
