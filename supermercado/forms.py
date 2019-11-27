from django import forms

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
