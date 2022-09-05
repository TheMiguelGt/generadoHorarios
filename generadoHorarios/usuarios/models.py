from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

# Create your models here.
class UserAlum(models.Model):
    idU = models.CharField(max_length=10, verbose_name="Id usuario")
    idTy = models.IntegerField(verbose_name="Id tipo")
    nom = models.CharField(max_length=100, verbose_name="Nombre")
    apePat = models.CharField(max_length=100, verbose_name="Apellido paterno")
    apeMat = models.CharField(max_length=100, verbose_name="Apellido materno")
    cPass = models.CharField(max_length=15, verbose_name="Password")
    email = models.CharField(max_length=100, verbose_name="Email")
    image = models.ImageField(verbose_name="Avatar", upload_to="usuarios") #aqui llevara todas las imagenes a media automaticamente
    grado = models.CharField(max_length=2,verbose_name="Grado")
    grupo = models.CharField(max_length=2,verbose_name="Grupo")
    turno = models.CharField(max_length=10,verbose_name="Turno")
    ciclo = models.CharField(max_length=5,verbose_name="Ciclo escolar")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    
    class Meta:
        verbose_name = "alumno"
        verbose_name_plural = "alumnos"
        ordering = ['idU','created']
        
    def __str__(self):
        return self.idU

class UserDoce(models.Model):
    idU = models.CharField(max_length=10, verbose_name="Id usuario")
    idTy = models.IntegerField(verbose_name="Id tipo")
    nom = models.CharField(max_length=100, verbose_name="Nombre")
    apePat = models.CharField(max_length=100, verbose_name="Apellido paterno")
    apeMat = models.CharField(max_length=100, verbose_name="Apellido materno")
    cPass = models.CharField(max_length=15, verbose_name="Password")
    email = models.CharField(max_length=100, verbose_name="Email")
    image = models.ImageField(verbose_name="Avatar", upload_to="usuarios") #aqui llevara todas las imagenes a media automaticamente
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "docente"
        verbose_name_plural = "docentes"
        ordering = ['idU','created']

    def __str__(self):
        return self.idU