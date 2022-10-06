from django.db import models

# Create your models here.

class Cargo(models.Model):
    description = models.CharField(max_length=50)
    salario = models.BigIntegerField()

class Horario(models.Model):
    h_llegada = models.DateTimeField()
    h_salida = models.DateTimeField()

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
    