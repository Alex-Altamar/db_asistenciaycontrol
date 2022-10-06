from django.db import models
from apps.empleados.models import empleado

# Create your models here.

class Adelanto(models.Model):
    f_adelannton = models.DateField()
    valor = models.BigIntegerField()
    empleado = models.ForeignKey(empleado, null= True, blank= True, on_delete=models.CASCADE)