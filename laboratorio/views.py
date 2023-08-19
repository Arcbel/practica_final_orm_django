from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Laboratorio, Producto, DirectorGeneral
from .forms import LaboratorioForm

# Create your views here.

def v_index(request):
    return render (request, 'index.html')

def v_info_labs(request):
    if 'numveces' in request.session:
        num = request.session['numveces']
    else:
        num = 0
    request.session['numveces'] = num + 1

    laboratorios = Laboratorio.objects.all()
    context = {
        'numveces': request.session['numveces'],
        'laboratorios': laboratorios
        }
    return render (request, 'informacion_labs.html', context)

def v_agregar(request):
    context = {
        'formulario': LaboratorioForm()
    }
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/info_labs')
    else:
        return render(request, 'agregar_lab.html', context)

def v_editar(request, laboratorio_id):
    laboratorio = Laboratorio.objects.get(id = laboratorio_id)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/info_labs')
    else:
        context = {
            'formedit' : LaboratorioForm(instance = laboratorio)
        }
        return render(request, 'editar_lab.html', context)

def v_eliminar(request, laboratorio_id):
    if request.method == 'POST':
        Producto.objects.filter(laboratorio = laboratorio_id).delete()
        DirectorGeneral.objects.filter(laboratorio = laboratorio_id).delete()
        Laboratorio.objects.get(id = laboratorio_id).delete()
        return HttpResponseRedirect('/info_labs')

    context = {
        'labs': Laboratorio.objects.get(id = laboratorio_id)
    }
    return render(request, 'eliminar_lab.html', context)