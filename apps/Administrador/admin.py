from django.contrib import admin
from apps.Administrador.models import Admin

# Register your models here.

class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('nombres','apellidos')

admin.site.register(Admin, AdministradorAdmin)