from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def v_index(request):
    return render (request, 'index.html')