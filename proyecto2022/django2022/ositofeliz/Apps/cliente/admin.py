from django.contrib import admin
from Apps.cliente.models import Cliente
from Apps.cliente.models import Comprar
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comprar)
admin.site.register(Cliente, ClienteAdmin)
