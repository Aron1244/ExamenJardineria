from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from . models import Usuario, Producto, Categoria

from . forms import UsuarioForm, CategoriaForm, ProductoForm

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

def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_superuser:
                # Si es superusuario, redirigir al panel de administración de Django
                return redirect('/admin/')
            elif user.username == 'adminTienda':
                # Si el usuario es 'admin1', redirigir a una template personalizada de administrador
                print(f"Usuario {username} autenticado como adminTienda")
                return render(request, 'verdevida/admin.html')
            else:
                # Si no es superusuario ni 'admin1', redirigir a la página de inicio
                return redirect('/')
        else:
            # Si la autenticación falla, mostrar mensaje de error
            error_message = 'Usuario o contraseña incorrectos.'
            return render(request, 'verdevida/login.html', {'error': error_message})
    
    # Si el método de solicitud no es POST, simplemente renderiza el formulario de inicio de sesión
    return render(request, 'verdevida/login.html')


def admin(request):
    context={}
    return render(request, 'verdevida/admin.html', context)

def crud_usuarios(request):

    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios}
    print("Enviando datos usuarios_list")
    return render(request, 'verdevida/usuarios_list.html', context)

def usuariosAdd(request):
    print("Estoy controlando usuariosAdd...")
    context={}

    if request.method == "POST":
        print("Controlador es un post...")
        form = UsuarioForm(request.POST)

        if form.is_valid:
            print("Estoy en agregar, is_valid")
            form.save()

            #limpiar forms
            form=UsuarioForm()

            context = {'mensaje':"Ok, datos grabados...", "form":form}
            return render(request, "verdevida/usuarios_add.html",context)
        else:
            context = {'form':form}
    else:
        form = UsuarioForm()
        context = {'form':form}
        return render(request, 'verdevida/usuarios_add.html',context)

def usuarios_del(request, pk):
    mensajes = []
    errores = []
    context = {}

    try:
        usuario = Usuario.objects.get(id_usuario=pk)
        usuario.delete()
        mensajes.append("Bien, datos eliminados...")
    except Usuario.DoesNotExist:
        errores.append("Error, id no existe")
    except Exception as e:
        errores.append(f"Error inesperado: {str(e)}")
    
    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios, 'mensajes': mensajes, 'errores': errores}
    return render(request, 'verdevida/usuarios_list.html', context)

def usuarios_edit(request,pk):
    try:
        usuario = Usuario.objects.get(id_usuario=pk)
        context = {}
        if usuario:
            print("Edit encontro el usuario...")
            if request.method == "POST":
                print("Edit, es un POST")
                form = UsuarioForm(request.POST, instance=usuario)
                form.save()
                mensaje = "Bien, datos actualizados..."
                print(mensaje)
                context = {'usuario':usuario, 'form':form, 'mensaje':mensaje}
                return render(request, 'verdevida/usuarios_edit.html', context)
            else:
                # no es un POST
                print("Edit, NO es un POST")
                form = UsuarioForm(instance=usuario)
                mensaje = ""
                context = {'usuario':usuario, 'form':form, 'mensaje':mensaje}
                return render(request, 'verdevida/usuarios_edit.html', context)
    except:
        print("Error, id no existe...")
        usuarios = Usuario.objects.all()
        mensaje = "Error, id no existe"
        context = {'mensaje':mensaje, 'usuarios':usuarios}
        return render(request, 'verdevida/usuarios_list.html', context)

# !CRUD categorias

def crud_categoria(request):

    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    print("Enviando datos categorias_list")
    return render(request, 'verdevida/categoria_list.html', context)

def categoriaAdd(request):
    print("Estoy controlando categoriaAdd...")
    context={}

    if request.method == "POST":
        print("Controlador es un post...")
        form = CategoriaForm(request.POST)

        if form.is_valid:
            print("Estoy en agregar, is_valid")
            form.save()

            #limpiar forms
            form=CategoriaForm()

            context = {'mensaje':"Ok, datos grabados...", "form":form}
            return render(request, "verdevida/categoria_add.html",context)
        else:
            context = {'form':form}
    else:
        form = CategoriaForm()
        context = {'form':form}
        return render(request, 'verdevida/categoria_add.html',context)

def categoria_del(request, pk):
    mensajes = []
    errores = []
    context = {}

    try:
        categoria = Categoria.objects.get(id_categoria=pk)
        categoria.delete()
        mensajes.append("Bien, datos eliminados...")
    except Categoria.DoesNotExist:
        errores.append("Error, id no existe")
    except Exception as e:
        errores.append(f"Error inesperado: {str(e)}")
    
    categorias = Categoria.objects.all()
    context = {'categorias': categorias, 'mensajes': mensajes, 'errores': errores}
    return render(request, 'verdevida/categoria_list.html', context)


def categoria_edit(request,pk):
    try:
        categoria = Categoria.objects.get(id_categoria=pk)
        context = {}
        if categoria:
            print("Edit encontró la categoria...")
            if request.method == "POST":
                print("Edit, es un POST")
                form = CategoriaForm(request.POST, instance=categoria)
                form.save()
                mensaje = "Bien, datos actualizados..."
                print(mensaje)
                context = {'categoria':categoria, 'form':form, 'mensaje':mensaje}
                return render(request, 'verdevida/categoria_edit.html', context)
            else:
                # no es un POST
                print("Edit, NO es un POST")
                form = CategoriaForm(instance=categoria)
                mensaje = ""
                context = {'categoria':categoria, 'form':form, 'mensaje':mensaje}
                return render(request, 'verdevida/categoria_edit.html', context)
    except:
        print("Error, id no existe...")
        categorias = Categoria.objects.all()
        mensaje = "Error, id no existe"
        context = {'mensaje':mensaje, 'categorias':categorias}
        return render(request, 'verdevida/categoria_list.html', context)

# !CRUD PRODUCTOS

def crud_producto(request):
    
    productos = Producto.objects.all()
    context = {'productos': productos}
    print("Enviado datos productos_list ....")
    return render(request, 'verdevida/producto_list.html', context)

def productosAdd(request):
    print("estoy controlando productosAdd")
    context={}

    if request.method == "POST":
        print("Controlador es un post...")
        form = ProductoForm(request.POST, request.FILES)

        if form.is_valid:
            print("Estoy en agregar, is_valid")
            form.save()

            #limpiando form
            form=ProductoForm()

            context = {'mensaje': "Ok, datos grabados", "form":form}
            return render(request, "verdevida/producto_add.html", context)
        else:
            context = {'form': form}

    else:
        form = ProductoForm()
        context = {'form':form}
        return render(request, 'verdevida/producto_add.html',context)
    


def producto_del(request, pk):
    mensajes = []
    errores = []
    context = {}

    try:
        producto = Producto.objects.get(id_producto=pk)
        producto.delete()
        mensajes.append("Bien, datos eliminados...")
    except Producto.DoesNotExist:
        errores.append("ERROR, id del producto no existe")
    except Exception as e:
        errores.append(f"ERROR inesperado: {str(e)}")
    
    productos = Producto.objects.all()
    context = {'productos': productos, 'mensajes': mensajes, 'errores': errores}
    return render(request, 'verdevida/producto_list.html', context)



def producto_edit(request, pk):
    try:
        producto = Producto.objects.get(id_producto=pk)
        context = {}
        if producto:
            print("edit encontro el producto...")
            if request.method == "POST":
                print("Edit, es un POST")
                form = ProductoForm(request.POST, request.FILES,instance=producto)
                if form.is_valid():
                    form.save()
                    mensaje = "Bien, datos actualizados..."
                    print(mensaje)
                    context = {'producto': producto, 'form': form, 'mensaje': mensaje}
                else:
                    mensaje = "Error, datos no válidos..."
                    context = {'producto': producto, 'form': form, 'mensaje': mensaje}
                return render(request, 'verdevida/producto_edit.html', context)
            else:
                # no post
                print("Edit, No es un post")
                form = ProductoForm(instance=producto)
                mensaje = ""
                context = {'producto': producto, 'form': form, 'mensaje': mensaje}
                return render(request, 'verdevida/producto_edit.html', context)
    except Producto.DoesNotExist:
        print("Error, id del producto no existe...")
        productos = Producto.objects.all()
        mensaje = "ERROR, id del producto no existe"
        context = {'mensaje': mensaje, 'productos': productos}
        return render(request, 'verdevida/producto_list.html', context)