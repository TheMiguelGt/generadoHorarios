from pyexpat import model
from django.db import models

# Create your models here.
class Plantel(models.Model):
    clave = models.CharField(max_length=10,null=False)
    plantel = models.CharField(max_length=45)

    class Meta:
        db_table = 'plantel'
    
    def __str__(self):
        return self.clave,self.plantel

class Licenciatura(models.Model):
    clave = models.CharField(max_length=10,null=False)
    licenciatura = models.CharField(max_length=45)
    plantel = models.ForeignKey(Plantel, null=False,on_delete=models.CASCADE)

    class Meta:
        db_table = 'licenciatura'

    def __str__(self):
        return self.clave,self.licenciatura,self.plantel

class Semestre(models.Model):
    semestre = models.CharField(max_length=1)
    licenciatura = models.ForeignKey(Licenciatura,null=False,on_delete=models.CASCADE)

    class Meta:
        db_table = 'semestre'

    def __str__(self):
        return self.semestre,self.licenciatura

class Aula(models.Model):
    clave = models.CharField(max_length=10,null=False)
    piso = models.CharField(max_length=2)
    plantel = models.ForeignKey(Plantel, null=False,on_delete=models.CASCADE)

    class Meta:
        db_table = 'aula'

    def __str__(self):
        return self.clave,self.piso,self.plantel


    