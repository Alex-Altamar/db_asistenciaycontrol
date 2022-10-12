from django.contrib import admin
from apps.adelantos.models import Adelanto
# Register your models here.

class AdelantoAdmin(admin.ModelAdmin):
    list_display = ('f_adelannton','empleado','valor')

admin.site.register(Adelanto, AdelantoAdmin)