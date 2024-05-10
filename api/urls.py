from django.urls import path,include
from rest_framework import routers
from api import views
'''
router = routers.DefaultRouter()
router.register(r'usuarios',views.UsuarioViewSet)'''

urlpatterns = [
    #path('', include(router.urls)),
    path('prueba/',views.Prueba.as_view()),
    path('add/', views.UsuarioAdd, name="add"),
    path('listar/', views.ListarUsuarios, name="listar")
    
]