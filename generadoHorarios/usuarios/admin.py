from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from import_export.admin import ImportExportModelAdmin,ImportForm,ImportExportActionModelAdmin
from .models import User,Admin,Coordina,Docente,Alumno
from .forms import UserForm,CoordinaProfileForm
# Register your models here.
@admin.register(User,Admin,Coordina,Docente)
class CoordinaAdmin(ImportExportActionModelAdmin):
    pass
    # list_display = ('password','email')
