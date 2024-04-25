from django.db import models

# Create your models here.
class usuario(models.Model):
    nickname =  models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    