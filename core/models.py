from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    apellido  = models.CharField(max_length=100, blank=True, null=True)
