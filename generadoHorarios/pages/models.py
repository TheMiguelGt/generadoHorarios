from pickle import FALSE
from tabnanny import verbose
from turtle import update
from django.db import models
from ckeditor.fields import RichTextField 
from registration.models import UserDoce,UserAlum

# Create your models here.
#modelo de materias
class Page(models.Model):
    idMateria = models.CharField(max_length=10,verbose_name="Clave de la materia",null=False)
    nomMateria = models.CharField(max_length=50, verbose_name="Nombre de la materia",null=False)
    numHoras = models.IntegerField(verbose_name="Numero de horas a la semana",null=False)
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
class DoceMate(models.Model):
    idMateria = models.ForeignKey(Page, null=True,blank=True, on_delete=models.CASCADE)
    idDoce = models.ForeignKey(UserDoce, null=True,blank=True, on_delete=models.CASCADE)
    preAca = models.CharField(max_length=250)

    class Meta:
        db_table = 'mate_doce'

    def __str__(self):
        return self.idMateria


