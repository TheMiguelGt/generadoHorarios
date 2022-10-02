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
    ROLES = (
        ('C','ADMIN'),
        ('D','DOCENTE'),
        ('E','ESTUDIANTE')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE) #identifica un perfil para cada usuario
    role = models.CharField(max_length=15,choices=ROLES, default='E')
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return self.role

@receiver(post_save,sender=User)#verificar usuario creado
def ensure_profile_exists(sender,instance,**kwargs):
    if kwargs.get('created',False):
        Profile.objects.get_or_create(user=instance)
        print("se acaba de crear un usuario y su perfil enlazado")
    