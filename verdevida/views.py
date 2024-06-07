from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request, 'verdevida/index.html', context)

def catalogo(request):
    context={}
    return render(request, 'verdevida/catalogo.html', context)

def contacto(request):
    context={}
    return render(request, 'verdevida/contacto.html', context)

def carrito(request):
    context={}
    return render(request, 'verdevida/carrito.html', context)

def crearUsuario(request):
    context={}
    return render(request, 'verdevida/crearUsuario.html', context)

def login(request):
    context={}
    return render(request, 'verdevida/login.html', context)

def suculenta(request):
    context={}
    return render(request, 'verdevida/suculenta.html', context)

def rosas(request):
    context={}
    return render(request, 'verdevida/rosas.html', context)

def macetero_negro(request):
    context={}
    return render(request, 'verdevida/macetero_negro.html', context)

def tierra_hojas(request):
    context={}
    return render(request, 'verdevida/tierra_hojas.html', context)

def arbusto(request):
    context={}
    return render(request, 'verdevida/arbusto.html', context)

def lillium(request):
    context={}
    return render(request, 'verdevida/lillium.html', context)