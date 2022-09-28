from django.db import models
from Apps.provedores.models import Provedores


# Create your models here.


class Producto(models.Model):
    codigo = models.CharField(max_length=50, verbose_name="Codigo")
    descripcion = models.CharField(max_length=300, verbose_name="Descripcion")
    precio = models.FloatField(verbose_name="Precio")
    
    

    def __str__(self):
        
        return self.codigo

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = " productos"

class Dirtribuir(models.Model):
    cantidad = models.IntegerField(verbose_name="Cantidad")
    codigoProvedores = models.ForeignKey(Provedores,  on_delete=models.CASCADE)
    codigo = models.ForeignKey(Producto,  on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo, self.codigoProvedores, self.cantidad

    class Meta:
        verbose_name = "Distribuir"
        verbose_name_plural = "Distribuciones"
        