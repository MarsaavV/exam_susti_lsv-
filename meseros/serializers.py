from rest_framework import serializers
from .models import Mesero

class MeseroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesero
        fields = ['nombre', 'edad', 'procedencia']  # Campos que queremos mostrar en la API
