from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
def custom_upload_to(instance,filename): #objeto que se esta guardando, fichero de la imagen que se sobreescribira
    old_instance = Profile.objects.get(pk=instance.pk)#eliminar la imagen anterior
    old_instance.avatar.delete()
    return 'profile/' + filename

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #identifica un perfil para cada usuario
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

@receiver(post_save,sender=User)#verificar usuario creado
def ensure_profile_exists(sender,instance,**kwargs):
    if kwargs.get('created',False):
        Profile.objects.get_or_create(user=instance)
        print("se acaba de crear un usuario y su perfil enlazado")
    