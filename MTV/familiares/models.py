from django.db import models

# Create your models here.
class Familiar (models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.FloatField() 
    vinculo = models.TextField(max_length=30)
    

