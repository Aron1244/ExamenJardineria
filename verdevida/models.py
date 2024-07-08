from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario      = models.AutoField(primary_key=True)
    nombre          = models.CharField(max_length=30)
    apellido        = models.CharField(max_length=30)
    fec_nac         = models.DateField(blank=False, null=False)
    direccion       = models.CharField(max_length=100)
    user_name       = models.CharField(max_length=20)
    correo          = models.EmailField(max_length=100)
    password        = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user_name)
    
class Categoria(models.Model):
    id_categoria        = models.AutoField(db_column='idCategoria', primary_key=True) 
    nombre_categoria    = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.nombre_categoria)

class Producto(models.Model):
    id_producto     = models.AutoField(primary_key=True)
    nombre_Producto = models.CharField(max_length=100)
    peso            = models.CharField(max_length=50)
    precio          = models.FloatField(max_length=15)
    categoria       = models.ForeignKey('Categoria', on_delete=models.CASCADE,db_column='idCategoria')
    portada         = models.ImageField(upload_to='portadas/', blank=True, null=True)
    cantidad        = models.IntegerField()

    def __str__(self):
        return str(self.nombre_Producto)