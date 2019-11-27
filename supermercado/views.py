from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ClienteForm,ProductoForm
from .models import Persona
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from apps.administrador.forms import registroform

# Create your views here.

def Inicio(request):
    return render(request,'supermercado/BASE.html')


def Agregar(request):
    cliente = ClienteForm()
    if request.method == 'POST':
        #informacion Formulario
        newcliente = ClienteForm(request.POST)
        if newcliente.is_valid():
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
            cliente = newcliente

    context = {
        'clienteform':cliente
    }  

    return render(request,#url la redireccion#,
    context)

#karina
 
def AdministradorRegistro_view(request):
    if request.method == 'POST':
        form = registroform(request.POST)
        if form.is_valid():
            from.save()
        return redirect('supermercado:Base.html')
     else: registroform()

     retun render(request,'supermercado/supermercado_form.html'), {'form': form})
            


