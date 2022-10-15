from django.shortcuts import render
from apps.empleados.models import empleado

# Create your views here.

def Listar_empleados(request):
    empleados = empleado.objects.all().order_by('-id')
    contex = {'empleados': empleados}
    return render(request, '', contex)
