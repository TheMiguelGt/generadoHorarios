from django.contrib import admin
from .models import UserAlum,UserDoce

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_diaplsy = ('idU','created')
    
admin.site.register(UserAlum,UserAdmin)
admin.site.register(UserDoce,UserAdmin)