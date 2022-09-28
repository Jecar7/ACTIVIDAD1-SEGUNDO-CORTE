from django.contrib import admin
from Apps.provedores.models import Provedores
# Register your models here

class ClienteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Provedores, ClienteAdmin)