from django.urls import path
from . import views

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('catalogo.html', views.catalogo, name='catalogo'),
    path('contacto.html', views.contacto, name='contacto'),
    path('carrito.html', views.carrito, name='carrito'),
    path('crearUsuario.html', views.crearUsuario, name='crearUsuario'),
    path('login.html', views.login, name='login'),
    path('suculenta.html', views.suculenta, name='suculenta'),
    path('rosas.html', views.rosas, name='rosas'),
    path('macetero_negro.html', views.macetero_negro, name='macetero_negro'),
    path('tierra_hojas.html', views.tierra_hojas, name='tierra_hojas'),
    path('arbusto.html', views.arbusto, name='arbusto'),
    path('lillium.html', views.lillium, name='lillium')
]