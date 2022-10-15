from django.shortcuts import render
from apps.empleados.models import empleado

# Create your views here.

def listempleados(request):
    empleados = empleado.objects.all().order_by('-id')
    contex = {'empleados': empleados}
    return render(request, 'empleados/listempleados.html', contex)

def home(request):
    return render(request, 'base/base.html')
