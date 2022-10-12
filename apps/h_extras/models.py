from django.db import models
from apps.empleados.models import empleado

# Create your models here.

class H_extra(models.Model):
    horas = models.BigIntegerField()
    valor = models.BigIntegerField()
    fecha = models.DateField()
    empleado = models.ForeignKey(empleado, null= True, blank= True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.fecha}{self.empleado}{self.horas}'