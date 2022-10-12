from django.contrib import admin
from apps.empleados.models import Cargo, Horario, empleado


# Register your models here.





admin.site.register(Cargo)
admin.site.register(Horario)
admin.site.register(empleado)