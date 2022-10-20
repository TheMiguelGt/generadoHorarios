from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse 
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_coordina = models.BooleanField(default=False)
    is_docente = models.BooleanField(default=False)
    is_alumno = models.BooleanField(default=False)
    
class Admin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Admin')
    nombre=models.CharField(max_length=50)
    apepat=models.CharField(max_length=50)
    apemat=models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    admin_profile_pic = models.ImageField(upload_to="usuarios/admin_profile_pic",blank=True)
    
    def get_absolute_url(self):
        return reverse("usuarios:admin_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.nombre,self.apepat,self.apemat
    
class Coordina(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Coordinador')
    nombre=models.CharField(max_length=50)
    apepat=models.CharField(max_length=50)
    apemat=models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    coordina_profile_pic = models.ImageField(upload_to="usuarios/cordina_profile_pic",blank=True)
    
    def get_absolute_url(self):
        return reverse("usuarios:coordina_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.nombre,self.apepat,self.apemat
    
class Docente(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Docente')
    nombre=models.CharField(max_length=50)
    apepat=models.CharField(max_length=50)
    apemat=models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    docente_profile_pic = models.ImageField(upload_to="usuarios/docente_profile_pic",blank=True)
    
    def get_absolute_url(self):
        return reverse("usuarios:docente_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.nombre,self.apepat,self.apemat

class Alumno(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Alumno')
    nombre=models.CharField(max_length=50)
    apepat=models.CharField(max_length=50)
    apemat=models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    alumno_profile_pic = models.ImageField(upload_to="usuarios/alumno_profile_pic",blank=True)
    
    def get_absolute_url(self):
        return reverse("usuarios:alumno_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.nombre,self.apepat,self.apemat
    

    