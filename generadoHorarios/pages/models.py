from pickle import FALSE
from tabnanny import verbose
from turtle import update
from django.db import models
from ckeditor.fields import RichTextField 
from registration.models import UserDoce,UserAlum
from institucion.models import Aula

# Create your models here.
#modelo de materias
class Page(models.Model):
    idMateria = models.CharField(max_length=10,verbose_name="Clave de la materia",null=False)
    nomMateria = models.CharField(max_length=50, verbose_name="Nombre de la materia",null=False)
    numHoras = models.IntegerField(verbose_name="Numero de horas a la semana",null=False)
    aula = models.ForeignKey(Aula,null=False,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    update = models.DateTimeField(auto_now="True", verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = 'materia'
        verbose_name_plural = 'materias'
        db_table = 'materia'
        ordering = ['idMateria','nomMateria']

    def __str__(self):
        return self.idMateria

#modelo de materia docente
class MateDispo(models.Model):
    materia = models.ForeignKey(Page, null=False,on_delete=models.CASCADE)
    docente = models.ForeignKey(UserDoce,null=False,on_delete=models.CASCADE)

    class Meta:
        db_table = 'materiaDisponible'

class Dia(models.Model):
    nomDia = models.CharField(max_length=15)
    
    class Meta:
        db_table = 'dia'
        
class Hora(models.Model):
    iniHora = models.CharField(max_length=10)
    finHora = models.CharField(max_length=10)
    
    class Meta:
        db_table = 'hora'
        
class DispoHora(models.Model):
    materia = models.ForeignKey(MateDispo,null=False,on_delete=models.CASCADE)
    dia = models.ForeignKey(Dia,null=False,on_delete=models.CASCADE)
    hora = models.ForeignKey(Hora,null=False,on_delete=models.CASCADE)

    class Meta:
        db_table = 'horaDisponible'