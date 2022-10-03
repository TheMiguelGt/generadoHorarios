from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save

# # Create your models here.
# def custom_upload_to(instance,filename): #objeto que se esta guardando, fichero de la imagen que se sobreescribira
#     old_instance = Profile.objects.get(pk=instance.pk)#eliminar la imagen anterior
#     old_instance.avatar.delete()
#     return 'profile/' + filename

# class Profile(models.Model):
#     ROLES = (
#         ('C','ADMIN'),
#         ('D','DOCENTE'),
#         ('E','ESTUDIANTE')
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE) #identifica un perfil para cada usuario
#     role = models.CharField(max_length=15,choices=ROLES, default='E')
#     avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)

#     class Meta:
#         db_table = 'usuarios'

#     def __str__(self):
#         return self.role

# @receiver(post_save,sender=User)#verificar usuario creado
# def ensure_profile_exists(sender,instance,**kwargs):
#     if kwargs.get('created',False):
#         Profile.objects.get_or_create(user=instance)
#         print("se acaba de crear un usuario y su perfil enlazado")

# Create your models here.
def custom_alum_upload_to(instance,filename): #objeto que se esta guardando, fichero de la imagen que se sobreescribira
    old_instance = Alumno.objects.get(pk=instance.pk)#eliminar la imagen anterior
    old_instance.avatar.delete()
    return 'profile/' + filename

class User(AbstractUser):
    is_alum = models.BooleanField(default=False)
    is_doce = models.BooleanField(default=False)
    is_coor = models.BooleanField(default=False)
    
class Alumno(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="Alumno")
    nombre = models.CharField(max_length=15)
    apepat = models.CharField(max_length=50)
    apemat = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to=custom_alum_upload_to, null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("alumno_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['roll_no']
        db_table = 'alumnos'
        
class Docente(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="Docente")
    nombre = models.CharField(max_length=15)
    apepat = models.CharField(max_length=50)
    apemat = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to=custom_alum_upload_to, null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("docente_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'docente'

    