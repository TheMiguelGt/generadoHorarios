from pickle import FALSE
from tabnanny import verbose
from turtle import update
from django.db import models
from ckeditor.fields import RichTextField 
from institucion.models import Aula
from usuarios.models import Docente
from simple_history.models import HistoricalRecords

# Create your models here.
#modelo de materias
class Page(models.Model):
    clave = models.CharField(max_length=10,null=False,unique=True)
    materia = models.CharField(max_length=45, verbose_name="Nombre de la materia")
    carga = models.IntegerField(null=False)
    history = HistoricalRecords()

    class Meta:
        db_table = 'pages_materia'

    def __str__(self):
        template = '{0.clave} {0.materia}'
        return template.format(self)

class DocenteMateria(models.Model):
    materia = models.ForeignKey(Page,null=False,on_delete=models.CASCADE,related_name='matdoce')
    docente = models.ForeignKey(Docente,null=False,on_delete=models.CASCADE,related_name='docedoce')
    aula = models.ForeignKey(Aula,null=False,on_delete=models.CASCADE,related_name='auladoce')
    history = HistoricalRecords()

    class Meta:
        db_table = 'pages_docenteMateria'

    def __str__(self):
        return self.materia,self.aula

class Dia(models.Model):
    dia = models.CharField(max_length=45,unique=True)
    history = HistoricalRecords()

    class Meta:
        db_table = 'pages_dia'

    def __str__(self):
        template = '{0.dia}'
        return template.format(self)

class Hora(models.Model):
    iniHora = models.CharField(max_length=45)
    finHora = models.CharField(max_length=45)
    history = HistoricalRecords()

    class Meta:
        db_table = 'pages_hora'

    def __str__(self):
        template = '{0.iniHora} - {0.finHora}'
        return template.format(self)

class Disponibilidad(models.Model):
    docente = models.ForeignKey(Docente,null=False,on_delete=models.CASCADE,related_name='doces')
    dia = models.ForeignKey(Dia,null=False,on_delete=models.CASCADE,related_name='days')
    hora = models.ForeignKey(Hora,null=False,on_delete=models.CASCADE,related_name='hours')
    history = HistoricalRecords()

    class Meta:
        db_table = 'pages_disponibilidad'

    def __str__(self):
        return self.dia,self.hora,self.docente