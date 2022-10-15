from django.urls import path
from apps.empleados.views import listempleados

app_name = 'Empleados'
urlpatterns = [
    path('',listempleados, name= 'listempleados'),
]