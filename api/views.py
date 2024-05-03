from rest_framework import viewsets
from .serializer import UsuariosSerializer
from .models import usuario
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuariosSerializer
    
class Register(viewsets.ModelViewSet):
    queryset = User.objects.all()


class Prueba(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        return Response("Exito")