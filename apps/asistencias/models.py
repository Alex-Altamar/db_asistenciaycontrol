from django.db import models
from apps.empleados.models import empleado

# Create your models here.


class Asistencia(models.Model):
    fecha = models.DateField()
    h_entrada = models.DateTimeField()
    status = models.BooleanField()
    h_salida = models.DateTimeField()
    n_horas = models.BigIntegerField()
    empleado = models.ForeignKey(empleado, null= True, blank= True, on_delete=models.CASCADE)
    