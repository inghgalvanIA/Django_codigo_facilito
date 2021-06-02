from django.http import HttpResponse
from django.shortcuts import render

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