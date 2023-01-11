from django.contrib import admin
from .models import Page,DocenteMateria
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
admin.site.register(Page,SimpleHistoryAdmin)

class DoceMateAdmin(admin.ModelAdmin):
    list_field = ['materia','docente']                                                        