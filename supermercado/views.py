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
      

#karina
# def AdministradorRegistro_view(request):
    # if request.method == 'POST':
    #     form = registroform(request.POST)
    #     if form.is_valid():
    #         from.save()
    #     return redirect('supermercado:Base.html')
    # else: registroform()

    #  retun render(request,'supermercado/supermercado_form.html'), {'form': form})