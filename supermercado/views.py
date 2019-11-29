from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ClienteForm,ProductoForm,UserForm
from .models import Persona,Producto,Genero,Comuna,Provincia,Region
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

#modificado por oscar
def traerGenero():
    generos = Genero.objects.all()
    return generos

def traerComuna():
    comuna = Comuna.objects.all()
    return comuna

def Inicio(request):
    return render(request,'supermercado/inicio/inicio.html')

def Login(request):
    return render(request,'supermercado/login/login.html')




def Agregar(request):
    userf = UserForm()
    cliente = ClienteForm()
    if request.method == 'POST':
        #informacion Formulario
        newcliente = ClienteForm(request.POST)
        newform = UserForm(data=request.POST)
        if  newform.is_valid() and newcliente.is_valid():
            value = newform.save()
            persona = Persona.objects.Create(
                run = newcliente.cleaned_data.get('run'),
                nombre = newcliente.cleaned_data.get('nombre'),
                apellido = newcliente.cleaned_data.get('apellido'),
                genero = newcliente.cleaned_data.get('genero'),
                correo = newcliente.cleaned_data.get('correo'),
                direccion = newcliente.cleaned_data.get('direccion'),
                comuna = newcliente.cleaned_data.get('comuna'),
                telefono = newcliente.cleaned_data.get('telefono'),
                tipo = newcliente.cleaned_data.get('tipo')
            )
            persona.save()
        else:
            cliente = newcliente(),
            userf = newform()
    context = {
        'clienteform':cliente,
        'userform':userf
    }  
    return render(request,"supermercado/inicio/registar.html",
    context)

def Agregar_pro(request):
    try:
        prod = agForm()
        if request.method == 'POST':
            newpro = agForm(request.POST)
            if newpro.is_valid():
                value = newpro.save()
                producto = Producto.objects.create(
                    nombre = newpro.cleaned_data.get('nombre')
                    descripcion= newpro.cleaned_data.get('descripcion')
                    stock= newpro.cleaned_data.get('stock')
                    precio = newpro.cleaned_data.get('precio')
                )
                producto.save()
      context = {
          'producto':prod
      }

    except ObjectDoesNotExist:
        return redirect('Inicio')


def buscar_pro(request,id):
    try:
        producto = Producto.objects.get(pk=id)
        if request.method == 'GET':
            pro = ProductoForm(instance=producto)
            print(pro)
            
            return render(request,'supermercado/inicio/busqueda.html',context={'producto':id})
        else:
            pro = ProductoForm(request.POST,instance = producto) 
            if pro.is_valid():
                pro.save()
                return redirect('') 
    except ObjectDoesNotExist:
        return redirect('Inicio')
      

def Agregaradministrador(request):
    userf = UserForm()
    administrador = administradorform()
    if request.method == 'POST':

        #informacion Formulario

        newadministrador = administradorform(request.POST)
        newform = UserForm(data=request.POST)
        if  newform.is_valid() and newadministrador.is_valid():
            value = newform.save()
            persona = Persona.objects.Create(
                nombre = newadministrador.cleaned_data.get('nombre'),
                apellido = newadministrador.cleaned_data.get('apellido'),
                run  = newadministrador.cleaned_data.get('run'),
                genero = newadministrador.cleaned_data.get('genero'),
                contraseña = newadministrador.cleaned_data.get('contraseña')
                correo = newadministrador.cleaned_data.get('correo'),
                direccion = newadministrador.cleaned_data.get('direccion'),
                telefono = newadministrador.cleaned_data.get('telefono'),
                cuidad = newadministrador.cleaned_data.get ('cuidad')
                comuna  = newadministrador.cleaned_data.get('comuna')
            )
            persona.save()
        else:
            administrador = newadministrador(),
            userf = newform()
    context = {
        'administradorform':administrador,
        'userform':userf
    }  
    return render(request,"supermercado/inicio/registar.html",
    context)

# modificar administrador
def modificaradministrador(request,idadministrador):
    try:
        administradorencontrado  = administrador.objects.get(pk=idadministrador)  
        form = administradorform(instance= administradorencontrado)
        if request.method =='POST':
            newform = administradorform(request.POST,instance=form)
            if  newform.is_valid ()  and newform.has.change():
                newform.save()
                messages.success(request,'usuario modificado correctamente!')
                return redirect ('inicioadministrador')
              else 

         context={  
             'form':newform
         }
         return render(request,'administrador/modificar.html', context)
      except  ObjectDoesNotExist:
          messages.warning(request,'usuario no existe')
          return  redirect('inicioadministrador')
         return render(request, 'administrador/modificar.html')  

 # eliminar administrador 

def eliminaradministrador(request,idadministrador):
    try:
        administradoreliminar = administrador.objects.get(pk=idadministrador)
        administradoreliminar.delete()
        messages.success(request,'usuario eliminado correctamente!')
        return redirect ('inicioadministrador')
     except ObjectDoesNotExist:
          messages.warning(request,'el usuario no existe')  
          return  redirect ('inicioadministrador')  




























    