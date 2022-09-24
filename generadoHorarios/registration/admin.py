from django.contrib import admin
from .models import UserCor,UserDoce,UserAlum

# Register your models here.
class CorAdmin(admin.ModelAdmin):
    ordering = ('idCor','idRol')

class DoceAdmin(admin.ModelAdmin):
    ordering = ('idDoce','idRol')

class AlumAdmin(admin.ModelAdmin):
    ordering = ('idAlum','idRol')

admin.site.register(UserCor, CorAdmin)
admin.site.register(UserDoce, DoceAdmin)
admin.site.register(UserAlum, AlumAdmin)
