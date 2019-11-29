"""configuracion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from supermercado.urls import path
from supermercado import views as vistaSupermercado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vistaSupermercado.Inicio,name='Inicio'),
    path('Login/', vistaSupermercado.Login,name='Login'),
    path('User/', vistaSupermercado.Agregar,name='User'),
    path('bus/<int:id>/',vistaSupermercado.buscar_pro,name='Bus'),
    path('agproduc/',vistaSupermercado.Agregar_pro, name='agproduc')
]
