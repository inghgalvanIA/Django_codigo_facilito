from django.http import HttpResponse
from django.shortcuts import render

def Index(request):
    return render(request, 'index.html',{
        #contexto
    "message":"Hola desde la vista",

    })