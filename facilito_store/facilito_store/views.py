from django.http import HttpResponse

def Index(request):
    return HttpResponse('Hola desde el archivo views.py')