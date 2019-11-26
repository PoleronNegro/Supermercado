from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from apps.administrador.forms import registroform

# Create your views here.

def Inicio(request):
    return render(request,'supermercado/BASE.html')



#karina
 
def AdministradorRegistro_view(request):
    if request.method == 'POST':
        form = registroform(request.POST)
        if form.is_valid():
            from.save()
        return redirect('supermercado:Base.html')
     else: registroform()

     retun render(request,'supermercado/supermercado_form.html'), {'form': form})
            


