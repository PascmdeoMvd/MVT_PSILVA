from django.db import models

# Create your models here.

class familiar(models.Model):
    nombre = models.CharField(_MAX_LENGTH=30)
    apellido = models.CharField(_MAX_LENGTH=30)
    fecha_nac = models.DateField()
    
    
    