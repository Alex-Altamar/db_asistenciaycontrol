from django.db import models

# Create your models here.

class Cargo(models.Model):
    description = models.CharField(max_length=50)
    salario = models.BigIntegerField()
    def __str__(self):
        return self.description

class Horario(models.Model):
    h_llegada = models.TimeField()
    h_salida = models.TimeField()
    
    def __str__(self) -> str:
        return f'{self.h_llegada}{self.h_salida}'

class empleado(models.Model):
    empleado_id = models.CharField(max_length=15)
    nombres = models.CharField(max_length=75)
    apellidos = models.CharField(max_length=75)
    direccion = models.CharField(max_length=20)
    f_nacimiento = models.DateField()
    foto = models.CharField(max_length=200)
    f_creacion = models.DateField()
    horario = models.ForeignKey(Horario,null= True, blank= True, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, null= True, blank= True, on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return self.nombres