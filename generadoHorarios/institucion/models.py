from pyexpat import model
from django.db import models

# Create your models here.
class Institucion(models.Model):
    clave = models.CharField(max_length=10,null=False)
    nombre = models.CharField(max_length=50,null=False)
    
    class Meta:
        db_table = 'plantel'
    
    def __str__(self):
        return self.clave
    
class Licenciatura(models.Model):
    claveLicenci = models.CharField(max_length=10,null=False)
    nomLicenci = models.CharField(max_length=50,null=False)
    calendario = models.CharField(max_length=5)
    plantel = models.ForeignKey(Institucion,null=False,on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'licenciatura'
    
    def __str__(self):
        return self.claveLicenci

class Grupo(models.Model):
    grupo = models.CharField(max_length=1,null=False)
    
    class Meta:
        db_table = 'grupo'

    def __str__(self):
        return self.grupo
    
class Aula(models.Model):
    claveAula = models.CharField(max_length=10,null=False)
    grupo = models.ForeignKey(Grupo,null=False,on_delete=models.CASCADE)
    licenciatura = models.ForeignKey(Licenciatura,null=False,on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'aula'
    
    def __str__(self):
        return self.claveAula