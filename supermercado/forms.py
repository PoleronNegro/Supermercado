from django import forms
from django.forms import ModelForm
from .models import Persona,Producto,Genero,Comuna
from django.contrib.auth.forms import AuthenticationForm 
# creado por karina 
# from apss.administrador.models import administrador

#creado por oscar(login)
class AuthenticationForm(ModelForm):
    


# class registroform(forms.modelsform):
#     class Meta:
#         model = administrador

#         fields=[
#             'nombre',
#             'apellido',
#             'run',
#             'genero',
#             'correo_electronico',
#             'direccion',
#             'telefono',
#             'cuidad',
#             'comuda',
#         ]

#         labels={
#                 'nombre' : 'Nombre',
#                 'apellido': 'Apellido',
#                 'run': 'Run',
#                 'genero':'Genero',
#                 'correo_electronico':'Correo_electronico',
#                 'direccion': 'Direccion',
#                 'telefono': 'Telefono',
#                 'ciudad': 'Cuidad'
#             }

        # widgtes= {
        #     'nombre': forms.TextInput(attrs=('class': 'form-control')),
        #     'apellido':forms.TextInput(attrs=('class': 'form-control')),
        #     'run':forms.TextInput(attrs=('class': 'form-control')),
        #     'genero':forms.checkboxselecmultiple(),
        #     'correo_electronico':forms.TextInput(attrs=('class': 'form-control')),
        #     'direccion':forms.TextInput(attrs=('class': 'form-control')),
        #     'telefono':forms.TextInput(attrs=('class': 'form-control')),
        #     'cuidad':forms.TextInput(attrs=('class': 'form-control')),
        #     }


def registrar(dato):
    for datos in dato:
        datos[dato].widgtes.attrs['class']='form-control'

class ClienteForm(ModelForm):
    def __init__(self,*arg,**kargs):
        super(ClienteForm,self).__init__(*args,**kargs)
        registrar(self.fields)

    run = forms.CharField(max_length=15,required=True,label='----------',help_text='no debe ser mayor a 15')
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
    def __init__(self,*arg,**kargs):
        super(ProductoForm,self).__init__(*args,**kargs)
        registrar(self.fields)

    nombre = forms.CharField(max_length=35,required=True,label='----------',help_text='no debe ser mayor a 30')


    class Meta:
        model = Producto
        fields =['producto_id','nombre']
