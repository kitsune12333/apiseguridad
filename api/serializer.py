from rest_framework import serializers
from .models import usuario

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = '__all__'