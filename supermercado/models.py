from django.db import models

# Create your models here.

class Genero(models.Model):
    tipo = models.CharField(max_length=15,null=False,blank=False)

class Region(models.Model):
    nombre_region = models.CharField(max_length=64,null=False,blank=False)
    num_regional = models.CharField(max_length=3,null=False,blank=False)

class Provincia(models.Model):
    nombre_provincia = models.CharField(max_length=64,null=False,blank=False)
    region = models.ForeignKey(Region,on_delete = models.CASCADE)

class Comuna(models.Model):
    nombre_comuna = models.CharField(max_length=64,null=False,blank=False)
    provincia = models.ForeignKey(Provincia,on_delete = models.CASCADE)

class Persona(models.Model):
    Run = models.CharField(primary_key=True,max_length=15,null=False,blank=False)
    nombre = models.CharField(max_length=25,null=False,blank=False)
    apellido = models.CharField(max_length=25,null=False,blank=False)
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    correo = models.CharField(max_length=50,null=False,blank=False)
    direccion = models.CharField(max_length=50,null=False,blank=False)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)
    telefono = models.CharField(max_length=12,null=False,blank=False)
    tipo = models.CharField(max_length=20,null=False,blank=False)
    puntos = models.IntegerField()

class Producto(models.Model):
    nombre = models.CharField(max_length=30,null=False,blank=False)
    descripcion = models.TextField(max_length=500,null=False,blank=False)
    stock = models.PositiveSmallIntegerField()
    precio = models.IntegerField()

class Boleta(models.Model):
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    rut = models.ForeignKey(Persona,on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=10,null=False,blank=False)
    fecha = models.DateTimeField(auto_now=True)
    total = models.PositiveIntegerField()

