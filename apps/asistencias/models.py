from django.db import models
from apps.empleados.models import empleado

# Create your models here.


class Asistencia(models.Model):
    fecha = models.DateField()
    h_entrada = models.TimeField(verbose_name='Hora de entrada')
    status = models.BooleanField()
    h_salida = models.TimeField(verbose_name='Hora de salida')
    n_horas = models.BigIntegerField()
    empleado = models.ForeignKey(empleado, null= True, blank= True, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.fecha},{self.empleado}'