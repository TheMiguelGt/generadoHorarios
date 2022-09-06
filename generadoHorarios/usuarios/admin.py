from django.contrib import admin
from .models import UserAlum,UserDoce

# Register your models here.
class AlumAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_diaplsy = ('idU','created')
    ordering = ('created','idU')
    search_fields = ('idU','apePat','ciclo')
    list_filter = ('idU','created','ciclo')

class DoceAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_diaplsy = ('idU','created')
    ordering = ('created','idU')
    search_fields = ('idU','apePat')
    list_filter = ('idU','created')
    
admin.site.register(UserAlum,AlumAdmin)
admin.site.register(UserDoce,DoceAdmin)