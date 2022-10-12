from dataclasses import field
from statistics import mode

from rest_framework import serializers
from Apps.clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"