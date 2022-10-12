from django.db import models


# Create your models here.

class Admin(models.Model):
    usuario = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=60)
    nombres = models.CharField(max_length=75)
    apellidos = models.CharField(max_length=75)
    foto = models.CharField(max_length=200)
    f_creacion = models.DateField()

    def __str__(self) -> str:
        return f'{self.nombres}{self.apellidos}'