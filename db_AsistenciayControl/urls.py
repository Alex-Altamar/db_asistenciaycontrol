"""db_AsistenciayControl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.empleados.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('empleados/', include('apps.empleados.urls'), name="empleados"),
    #path('Administrador/', include('apps.Administrador.urls'), name="Administrador"),
    
    #ubicamos namespace y lo referencio en archivo patterns y agrego nombre en url del modelo
]
