from django.contrib import admin
from apps.empleados.models import Cargo, Horario, empleado


# Register your models here.

class empleadoAdmin(admin.ModelAdmin):
    list_display = ('nombres','apellidos','cargo','horario')
    ordering = ('nombres','apellidos','cargo','horario',)
    search_fields = ['nombres','apellidos','cargo__description',]#dos guiones debajo para realizar la busqueda cuandohay una llave foranea dentro de la tabla en la que de va a ralizar el filtro de busqueda###
    list_filter = ('nombres','cargo',)


admin.site.register(Cargo)
admin.site.register(Horario)
admin.site.register(empleado, empleadoAdmin)