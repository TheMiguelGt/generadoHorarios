from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from .choices import rol

# Create your models here.
def custom_upload_to(instance,filename): #objeto que se esta guardando, fichero de la imagen que se sobreescribira
    old_instance = Profile.objects.get(pk=instance.pk)#eliminar la imagen anterior
    old_instance.avatar.delete()
    return 'profile/' + filename

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #identifica un perfil para cada usuario
    userNom = models.CharField(max_length=50, verbose_name="Nombre")
    userApepat = models.CharField(max_length=50, verbose_name="Apellido paterno")
    userApemat = models.CharField(max_length=50, verbose_name="Apellido materno")
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)

    class Meta:
        db_table = 'usuarios'

#usuario coordinador
class UserCor(models.Model):
    idCor = models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)
    idRol = models.CharField(max_length=1, choices=rol, default='M')

    class Meta:
        db_table = "coordinador"

    def __str__(self):
        return self.idCor

#usuario docente
class UserDoce(models.Model):
    idDoce = models.ForeignKey(Profile,null=False,on_delete=models.CASCADE)
    idRol = models.CharField(max_length=1, choices=rol, default='M')
    numHoras = models.IntegerField(verbose_name="Numero de horas a la semana")

    class Meta:
        db_table = "docente"

    def __str__(self):
        return self.idDoce

#usuario alumno
class UserAlum(models.Model):
    idAlum = models.ForeignKey(Profile,null=False,on_delete=models.CASCADE)
    idRol = models.CharField(max_length=1, choices=rol, default='A')

    class Meta:
        db_table = "alumno"

    def __str__(self):
        return self.idAlum

@receiver(post_save,sender=User)#verificar usuario creado
def ensure_profile_exists(sender,instance,**kwargs):
    if kwargs.get('created',False):
        Profile.objects.get_or_create(user=instance)
        print("se acaba de crear un usuario y su perfil enlazado")
    