from rest_framework import viewsets
from .serializer import UsuariosSerializer
from .models import usuario

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = UsuariosSerializer