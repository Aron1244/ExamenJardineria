from django.urls import path
from . import views

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('catalogo.html', views.catalogo, name='catalogo'),
    path('contacto.html', views.contacto, name='contacto'),
    path('carrito.html', views.carrito, name='carrito'),
    path('crearUsuario.html', views.crearUsuario, name='crearUsuario'),
    path('login.html', views.custom_login_view, name='login'),
    path('suculenta.html', views.suculenta, name='suculenta'),
    path('rosas.html', views.rosas, name='rosas'),
    path('macetero_negro.html', views.macetero_negro, name='macetero_negro'),
    path('tierra_hojas.html', views.tierra_hojas, name='tierra_hojas'),
    path('arbusto.html', views.arbusto, name='arbusto'),
    path('lillium.html', views.lillium, name='lillium'),
    path('admin.html', views.admin, name='admin'),
    path('crud_usuarios', views.crud_usuarios, name='crud_usuarios'),
    path('usuariosAdd', views.usuariosAdd, name='usuariosAdd'),
    path('usuarios_del/<str:pk>',views.usuarios_del,name='usuarios_del'),
    path('usuarios_edit/<str:pk>',views.usuarios_edit,name='usuarios_edit'),
    path('crud_categoria', views.crud_categoria, name='crud_categoria'),
    path('categoriaAdd', views.categoriaAdd, name='categoriaAdd'),
    path('categoria_del/<str:pk>',views.categoria_del,name='categoria_del'),
    path('categoria_edit/<str:pk>',views.categoria_edit,name='categoria_edit'),
    path('crud_producto', views.crud_producto, name='crud_producto'),
    path('productosAdd', views.productosAdd, name='productosAdd'),
    path('producto_del/<str:pk>', views.producto_del, name='producto_del'),
    path('producto_edit/<str:pk>', views.producto_edit, name='producto_edit'),
]