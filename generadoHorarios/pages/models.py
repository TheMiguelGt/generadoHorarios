from pickle import FALSE
from tabnanny import verbose
from turtle import update
from django.db import models
from ckeditor.fields import RichTextField 
from institucion.models import Aula,Licenciatura,Semestre
from usuarios.models import Docente
from simple_history.models import HistoricalRecords

# Create your models here.
#modelo de materias
class Page(models.Model):
    clave = models.CharField(max_length=10,null=False,unique=True)
    materia = models.CharField(max_length=45, verbose_name="Nombre de la materia")
    carga = models.IntegerField(null=False)
    aula = models.CharField(max_length=10,null=False)
    history = HistoricalRecords()

    class Meta:
        db_table = 'pages_materia'

    def __str__(self):
        template = '{0.materia}'
        return template.format(self)

class DocenteMateria(models.Model):
    materia = models.ForeignKey(Page,null=False,on_delete=models.CASCADE,related_name='matdoce')
    docente = models.ForeignKey(Docente,null=False,on_delete=models.CASCADE,related_name='docedoce')
    clase = models.ForeignKey(Semestre,null=False,on_delete=models.CASCADE)
    start_time = models.PositiveBigIntegerField(null=False)
    end_time = models.PositiveBigIntegerField(null=False)
    dia = models.CharField(max_length=10,null=False)
    history = HistoricalRecords()

    class Meta:
        db_table = 'pages_docenteMateria'

    def __str__(self):
        template = '{0.materia}  {0.docente}'
        return template.format(self)

class Dia(models.Model):
    dia = models.CharField(max_length=45,unique=True)
    history = HistoricalRecords()

    class Meta:
        db_table = 'pages_dia'

    def __str__(self):
        template = '{0.dia}'
        return template.format(self)

class Hora(models.Model):
    iniHora = models.CharField(max_length=45,unique=True)
    finHora = models.CharField(max_length=45,unique=True)
    history = HistoricalRecords()

    class Meta:
        db_table = 'pages_hora'

    def __str__(self):
        template = '{0.iniHora} - {0.finHora}'
        return template.format(self)

class Disponibilidad(models.Model):
    docente = models.ForeignKey(Docente,null=False,on_delete=models.CASCADE,related_name='doces')
    dia = models.ForeignKey(Dia,null=False,on_delete=models.CASCADE,related_name='days')
    horaini = models.CharField(max_length=5)
    horafin = models.CharField(max_length=5)
    semestre = models.ForeignKey(Semestre,null=False,on_delete=models.CASCADE,related_name='sem')
    licenciatura = models.ForeignKey(Licenciatura,null=False,on_delete=models.CASCADE,related_name='licen')
    history = HistoricalRecords()

    class Meta:
        db_table = 'pages_disponibilidad'

    def __str__(self):
        return self.dia,self.horaini,self.horafin,self.docente