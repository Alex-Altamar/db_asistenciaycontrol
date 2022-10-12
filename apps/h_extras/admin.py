from django.contrib import admin
from apps.h_extras.models import H_extra

# Register your models here.

class H_extraAdmin(admin.ModelAdmin):
    list_display = ('empleado','fecha','horas','valor')

admin.site.register(H_extra, H_extraAdmin)