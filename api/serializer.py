from rest_framework import serializers


from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        EMAIL_FIELD = 'username'
        REQUIRED_FIELDS = ['email', 'password', 'username']
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        
        user.save()
        return user 