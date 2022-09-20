from tabnanny import verbose
from turtle import update
from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.
class Page(models.Model):
    idMateria = models.CharField(primary_key=True,max_length=10,verbose_name="Clave de la materia",default="")
    nomMateria = models.CharField(max_length=50, verbose_name="Nombre de la materia",null=True)
    numHoras = models.IntegerField(verbose_name="Numero de horas a la semana",null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    update = models.DateTimeField(auto_now="True", verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = 'materia'
        verbose_name_plural = 'materias'
        db_table = 'materia'
        ordering = ['idMateria','nomMateria']

    def __str__(self):
        return self.idMateria
