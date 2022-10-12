from django.db import models

# Create your models here.

class Deduccion(models.Model):
    descripcion = models.CharField(max_length=50)
    valor = models.BigIntegerField()

    def __str__(self) -> str:
        return self.descripcion, self.valor