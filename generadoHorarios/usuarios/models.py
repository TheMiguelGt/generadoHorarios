from email.policy import default
from re import template
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import model_to_dict
from django.urls import reverse 
from django.conf import settings
from simple_history.models import HistoricalRecords

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_coordina = models.BooleanField(default=False)
    is_docente = models.BooleanField(default=False)
    is_alumno = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_usuario'
    
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

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'user_administrador'
        default_permissions = ('add','change','delete','view')
    
class Coordina(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Coordinador')
    nombre=models.CharField(max_length=50)
    apepat=models.CharField(max_length=50)
    apemat=models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    coordina_profile_pic = models.ImageField(upload_to="usuarios/cordina_profile_pic",blank=True)
    history = HistoricalRecords()
    
    def get_absolute_url(self):
        return reverse("usuarios:coordina_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.nombre,self.apepat,self.apemat

    class Meta:
        db_table = 'user_coordinador'
        default_permissions = ('add','change','delete','view')
    
class Docente(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Docente')
    nombre=models.CharField(max_length=50)
    apepat=models.CharField(max_length=50)
    apemat=models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    docente_profile_pic = models.ImageField(upload_to="usuarios/docente_profile_pic",blank=True)
    history = HistoricalRecords()
    
    def get_absolute_url(self):
        return reverse("usuarios:docente_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        template = '{0.nombre} {0.apepat} {0.apemat}'
        return template.format(self)

    class Meta:
        db_table = 'user_docente'
        default_permissions = ('add','change','delete','view')

class Alumno(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Alumno')
    nombre=models.CharField(max_length=50)
    apepat=models.CharField(max_length=50)
    apemat=models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    alumno_profile_pic = models.ImageField(upload_to="usuarios/alumno_profile_pic",blank=True)
    history = HistoricalRecords()
    
    def get_absolute_url(self):
        return reverse("usuarios:alumno_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.nombre,self.apepat,self.apemat

    class Meta:
        db_table = 'user_alumno'
        default_permissions = ('change','view')

class History(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=50)
    prev = models.CharField(max_length=50)
    new = models.CharField(max_length=50)

    @property
    def _history_user(self):
        return self.user

    def __str__(self):
        return self.user,self.time,self.type

    class Meta:
        db_table = 'user_history'

    