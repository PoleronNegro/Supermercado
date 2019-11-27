from django import forms
<<<<<<< HEAD
from django.forms import ModelForm
from .models import Persona,Producto



def registrar(datos):
    for datos in dato:
        dato[datos].widget.attrs['class'] = 'form-control'


#registrar
class ClienteForm(ModelForm):
    def __init__(self,*args,**kargs):
        super(ClienteForm,self).__init__(*args,**kargs)
        registrar(self.fields)

    run = forms.CharField(max_length=15,required=True,label='Ingrese run',help_text='----')
    nombre = forms.CharField(max_length=25,required=True,label='Ingrese nombres',help_text='los nombres no puede ser mayor a 30 caracteres')
    apellido = forms.CharField(max_length=25,required=True,label='Ingrese apellidos',help_text='los apellidos no puede ser mayor a 25 caracteres')
    genero = forms.ModelChoiceField(queryset = Genero.objects.all(),label='Seleccione su genero',required=True)
    correo = forms.CharField(max_length=50,required=True,label='Ingrese su correo',help_text='correo no debe ser mayor a 50 caracteres')
    direccion = forms.CharField(max_length=50,required=True,label='Ingrese su direccion',help_text='la direccion no puede ser mayor a 50 caracteres')
    comuna = forms.ModelChoiceField(queryset = nombre_comuna.objects.all(),label='Selecione comuna',required=True)  
    telefono = forms.CharField(max_length=12,required=True,label='Ingrese su telefono',help_text='numero telefonico no mayor a 12')
    tipo = forms.CharField(max_length=20,required=True,label='tipo',help_text='no puede ser mayor a 20 caracteres')      

    class Meta:
        model = Persona
        fields = ['run','nombre','apellido','genero','correo','direccion','comuna','telefono','tipo']    


class ProductoForm(ModelForm):
    def __init__(self,*args,**kargs):
        super(ProductoForm,self).__init__(*args,**kargs)
        registrar(self.fields)

    class Meta:
        model = Producto
        fields = ['id_producto']    
=======

# creado por karina 
from apss.administrador.models import administrador


class  registroform (forms.modelsform)
class Meta:
    model = administrador

    fields=[
        'nombre',
        'apellido',
        'run',
        'genero',
        'correo_electronico',
        'direccion',
        'telefono',
        'cuidad',
        'comuda',
        
    ]

    labels={
        'nombre' : 'Nombre',
        'apellido': 'Apellido',
        'run': 'Run',
        'genero':'Genero',
        'correo_electronico':'Correo_electronico',
        'direccion': 'Direccion',
        'telefono': 'Telefono',
        'ciudad': 'Cuidad'
    }

    widgtes= {
        'nombre': forms.TextInput(attrs=('class': 'form-control')),
        'apellido':forms.TextInput(attrs=('class': 'form-control')),,
        'run':forms.TextInput(attrs=('class': 'form-control')),,
        'genero':forms.checkboxselecmultiple(),
        'correo_electronico':forms.TextInput(attrs=('class': 'form-control')),,
        'direccion':forms.TextInput(attrs=('class': 'form-control')),,
        'telefono':forms.TextInput(attrs=('class': 'form-control')),,
        'cuidad':forms.TextInput(attrs=('class': 'form-control')),,

    }
>>>>>>> 6dda2107398ba729d43264004c2d539e954a05e3
