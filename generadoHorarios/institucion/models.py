from pyexpat import model
from re import template
from django.db import models

# Create your models here.
class Plantel(models.Model):
    clave = models.CharField(max_length=10,null=False)
    plantel = models.CharField(max_length=200)

    class Meta:
        db_table = 'plantel'
    
    def __str__(self):
        template = '{0.plantel}'
        return template.format(self)

class Licenciatura(models.Model):
    clave = models.CharField(max_length=10,null=False)
    licenciatura = models.CharField(max_length=45)
    plantel = models.ForeignKey(Plantel, null=False,on_delete=models.CASCADE,max_length=200)

    class Meta:
        db_table = 'licenciatura'

    def __str__(self):
        template = '{0.licenciatura}'
        return template.format(self)

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
        template = '{0.clave} en {0.plantel}'
        return template.format(self)


    
