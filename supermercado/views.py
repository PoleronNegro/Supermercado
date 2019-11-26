from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def Inicio(request):
    return render(request,'supermercado/BASE.html')

