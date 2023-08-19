from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Laboratorio
from .forms import LaboratorioForm

# Create your views here.

def v_index(request):
    return render (request, 'index.html')

def v_info_labs(request):
    laboratorios = Laboratorio.objects.all()
    context = {'laboratorios': laboratorios}
    return render (request, 'informacion_labs.html', context)

def v_agregar(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/info_labs')
    else:
        form = LaboratorioForm
        return render(request, 'agregar_lab.html', {'form': form})

