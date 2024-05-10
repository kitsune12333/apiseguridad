from rest_framework import viewsets
from .serializer import UsuariosSerializer
from .models import Usuario
from api.models import Usuario
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
"""
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuariosSerializer"""
    
class Register(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()


class Prueba(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        return Response("Exito")
    
@api_view(["POST"])
def UsuarioAdd(request):
    serializer = UsuariosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(["GET"])
def ListarUsuarios(request):
    usuarios = Usuario.objects.all()
    serializer = UsuariosSerializer(usuarios, many=True)
    return Response(serializer.data)