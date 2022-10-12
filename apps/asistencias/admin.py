from django.contrib import admin
from apps.asistencias.models import Asistencia

# Register your models here.

class asisteciaAdmin(admin.ModelAdmin):
    list_display = ('fecha','h_entrada','h_salida','empleado')


admin.site.register(Asistencia, asisteciaAdmin)