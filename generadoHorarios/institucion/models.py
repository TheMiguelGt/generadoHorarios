from pyexpat import model
from re import template
from django.db import models
from simple_history.models import HistoricalRecords
from multiselectfield import MultiSelectField

# Create your models here.
class Plantel(models.Model):
    clave = models.CharField(max_length=10,null=False,unique=True)
    plantel = models.CharField(max_length=200)
    history = HistoricalRecords()

    class Meta:
        db_table = 'institucion_plantel'
    
    def __str__(self):
        template = '{0.clave} {0.plantel}'
        return template.format(self)

class Licenciatura(models.Model):
    clave = models.CharField(max_length=10,null=False,unique=True)
    licenciatura = models.CharField(max_length=45)
    plantel = models.ForeignKey(Plantel, null=False,on_delete=models.CASCADE,max_length=200)
    history = HistoricalRecords()

    class Meta:
        db_table = 'institucion_licenciatura'

    def __str__(self):
        template = '{0.licenciatura}'
        return template.format(self)

class Semestre(models.Model):
    WEEK_DAY = (
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miercoles', 'Miercoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sabado', 'Sabado')
    )
    semestre = models.CharField(max_length=1)
    licenciatura = models.ForeignKey(Licenciatura,null=False,on_delete=models.CASCADE)
    ciclo = models.CharField(max_length=5,null=False)
    week_day = MultiSelectField(max_length=2000,choices=WEEK_DAY,max_choices=6)
    start_time = models.PositiveBigIntegerField(null=True)
    end_time = models.PositiveBigIntegerField(null=True)
    history = HistoricalRecords()

    class Meta:
        db_table = 'institucion_semestre'

    def __str__(self):
        template = 'Semestre {0.semestre} de la licenciatura en {0.licenciatura} con el ciclo {0.ciclo}'
        return template.format(self)
        # template = '{0.semestre}'
        # return template.format(self)

class Aula(models.Model):
    clave = models.CharField(max_length=10,null=False,unique=True)
    piso = models.CharField(max_length=2)
    plantel = models.ForeignKey(Plantel, null=False,on_delete=models.CASCADE)
    history = HistoricalRecords()

    class Meta:
        db_table = 'institucion_aula'

    def __str__(self):
        template = '{0.clave}'
        return template.format(self)


    
