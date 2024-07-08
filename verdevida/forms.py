from django import forms
from . models import Usuario,Categoria,Producto

from django.forms import ModelForm


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ["nombre","apellido","fec_nac","direccion","user_name","password","correo"]
        labels = {'nombre':'Nombre', 'fec_nac':'Fecha nacimiento', 'direccion':'Dirección', 'user_name':'Nombre usuario','password':'Contraseña'}

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre_categoria",]
        labels = {'nombre_categoria':'Categoría', }

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre_Producto", "peso","precio","categoria","portada","cantidad"]
        labels = {'nombre_Producto':'Nombre', 'peso':'Peso','precio': 'Precio','Categoria':'Categoría','Portada':'Portada'}