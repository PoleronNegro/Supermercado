from django import forms
from django.forms import ModelForm
from .models import Persona,Producto,Genero,Comuna
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm 
from django.contrib.auth.forms import User

def control(dato):
    for datos in dato:
        dato[datos].widget.attrs['class']='form-control'

#creado por oscar(login)
# class AuthenticationForm(ModelForm):


class UserForm(UserCreationForm):
    def __init__(self,*args,**kargs):
        super(UserForm,self).__init__(*args,**kargs)
        control(self.fields)

    class Meta:
        model = User
        fields = ['username','password1','password2']
  

class ClienteForm(ModelForm):
    def __init__(self,*args,**kargs):
        super(ClienteForm,self).__init__(*args,**kargs)
        control(self.fields)

    run = forms.CharField(max_length=10,required=True,label='--run--',help_text='no debe ser mayor a 15')
    nombre = forms.CharField(max_length=20,required=True,label='Ingrese nombres',help_text='no puede ser mayor a 20')
    apellido = forms.CharField(max_length=20,required=True,label='Ingrese apellidos',help_text='no puede ser mayor a 20')
    genero = forms.ModelChoiceField(queryset = Genero.objects.all(),label='Seleccione su genero',required=True) 
    correo = forms.CharField(max_length=50,required=True,label='Ingrese correo',help_text='')
    direccion = forms.CharField(max_length=50,required=True,label='Ingrese direccion',help_text='------')
    comuna = forms.ModelChoiceField(queryset = Comuna.objects.all(),label='Seleccione su comuna',required=True)
    telefono = forms.CharField(max_length=12,required=True,label='agrege su numero telefonico',help_text='no puede ser mayor a 12 caracteres')   
    tipo= forms.CharField(max_length=20,required=True,label='tipo',help_text='----')   

    class Meta:
        model = Persona
        fields = ['run','nombre','apellido','genero','correo','direccion','comuna','telefono','tipo']


class ProductoForm(ModelForm):
    def __init__(self,*args,**kargs):
        super(ProductoForm,self).__init__(*args,**kargs)
        control(self.fields)

    nombre = forms.CharField(max_length=35,required=True,label='nombre producto',help_text='no debe ser mayor a 30')


    class Meta:
        model = Producto
        fields =['id', 'nombre']



class agForm(ModelForm):
    def __init__(self,*args,**kargs):
        super(ProductoForm,self).__init__(*args,**kargs)
        control(self.fields)
    
    
    nombre = forms.CharField(max_length=35,required=True,label='nombre producto',help_text='no debe ser mayor a 30')
    descripcion = forms.TextField(max_length=256,label='descripcion')
    stock= PositiveSmallIntegerField()
    precio = forms.IntegerField()

    class Meta:
        model = Producto
        fields =['nombre','descripcion','stock','precio']



 class administradorform(ModelForm):
    def __init__(self,*args,**kargs):
        super(administradorform,self).__init__(*args,**kargs)
        control(self.fields)

    nombre = forms.CharField(max_length=20,required=True,label='Ingrese nombres',help_text='no puede ser mayor a 20')
    apellido = forms.CharField(max_length=20,required=True,label='Ingrese apellidos',help_text='no puede ser mayor a 20')
    run = forms.CharField(max_length=10,required=True,label='--run--',help_text='no debe ser mayor a 15')
    genero = forms.ModelChoiceField(queryset = Genero.objects.all(),label='Seleccione su genero',required=True) 
    contraseña =  forms.CharField(max_length=50,required=True,label='Ingrese contraseña',help_text=''))
    correo  = forms.CharField(max_length=50,required=True,label='Ingrese correo',help_text='')
    direccion  = forms.CharField(max_length=50,required=True,label='Ingrese direccion',help_text='------')
    telefono = forms.CharField(max_length=12,required=True,label='agrege su numero telefonico',help_text='no puede ser mayor a 12 caracteres')   
    comuna= forms.ModelChoiceField(queryset = Comuna.objects.all(),label='Seleccione su comuna',required=True)
    cuidad =  forms.ModelChoiceField(queryset= cuidad.objects.all(), label ='selecione su cuidad', requided=True)

    class Meta:
        model = Persona
        fields = ['nombre','apellido','run','genero','contraseña' ,'correo','direccion','telefono','comuna','cuidad']
       
    
    
