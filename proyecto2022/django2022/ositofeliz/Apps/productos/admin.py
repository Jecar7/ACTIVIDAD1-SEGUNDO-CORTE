from django.contrib import admin
from Apps.productos.models import Producto, Dirtribuir
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Dirtribuir)
admin.site.register(Producto, ClienteAdmin)
