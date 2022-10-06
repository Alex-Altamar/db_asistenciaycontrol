from django.db import models

# Create your models here.

class Deduccion(models.Model):
    descripcion = models.CharField(max_length=50)
    valor = models.BigIntegerField()