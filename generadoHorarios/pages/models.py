from pickle import FALSE
from tabnanny import verbose
from turtle import update
from django.db import models
from ckeditor.fields import RichTextField 
from institucion.models import Aula

# Create your models here.
#modelo de materias
class Page(models.Model):
    clave = models.CharField(max_length=10,null=False)
    materia = models.CharField(max_length=45, verbose_name="Nombre de la materia")
    carga = models.IntegerField(null=False)

    class Meta:
        db_table = 'materia'

    def __str__(self):
        return self.clave,self.materia,self.carga

class DocenteMateria(models.Model):
    materia = models.ForeignKey(Page,null=False,on_delete=models.CASCADE)
    # docente = models.ForeignKey(Docente,null=False,on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula,null=False,on_delete=models.CASCADE)

    class Meta:
        db_table = 'docenteMateria'

    def __str__(self):
        return self.materia,self.aula

class Dia(models.Model):
    dia = models.CharField(max_length=45)

    class Meta:
        db_table = 'dia'

    def __str__(self):
        return self.dia

class Hora(models.Model):
    hora = models.CharField(max_length=45)

    class Meta:
        db_table = 'hora'

    def __str__(self):
        return self.hora

class disponibilidad(models.Model):
    # docente = models.ForeignKey(Docente,null=False,on_delete=models.CASCADE)
    dia = models.ForeignKey(Dia,null=False,on_delete=models.CASCADE)
    hora = models.ForeignKey(Hora,null=False,on_delete=models.CASCADE)

    class Meta:
        db_table = 'disponibilidad'

    def __str__(self):
        return self.dia,self.hora