from django.urls import path
from Apps.cliente.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]
