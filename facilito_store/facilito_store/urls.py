
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index ,name='Index'),
    path('admin/', admin.site.urls),
    path('usuarios/login', views.login ,name='login'),
    
]
