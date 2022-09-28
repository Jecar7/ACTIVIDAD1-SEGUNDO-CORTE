from django.db import models

# Create your models here.


class Provedores(models.Model):
    codigoProvedores = models.CharField(max_length=50, help_text="Ingrese el codigo del Provedor")
    nombreProvedores = models.CharField(max_length=100, help_text="Ingrese el Nombre del Provedores")
    apellidoProvedores = models.CharField(max_length=100, help_text="Ingrese el apellido del Provedores")
    direccionProvedores = models.CharField(max_length=100, help_text="Ingrese la Direccion del Provedores")
    provinciaProvedores = models.CharField(max_length=100, help_text="Ingrese el Provincia del Provedores")
    telefonoProvedores = models.CharField(max_length=12, help_text="Ingrese el Telefono del Provedores")
    
    

    def __str__(self):
        return self.nombreProvedores
    

    class Meta:
        verbose_name = "Provedores"
        verbose_name_plural = "Provedores"
        
