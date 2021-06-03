from django.http import HttpResponse
from django.shortcuts import render

#todas las funciones asociadas a una ruta llevara el request

def Index(request):
    return render(request, 'index.html',{
        #contexto
    "message":"Listado de Productos",
    "title":"Productos",
    "productos":[
        {"title":"Playera","price":5,"stock":True},
        {"title":"Camisa","price":7,"stock":True},
        {"title":"Mochila","price":20,"stock":False},
    ]

    })

def login(request):
    return render(request, 'users/login.html',{
        
    })
