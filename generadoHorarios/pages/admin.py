from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created','update')
    list_display = ('idMateria','nomMateria','numHoras','created')
    ordering = ('idMateria','nomMateria')
    search_fields = ('nomMateria','created')
    list_filter = ('idMateria','nomMateria','numHoras')
    
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

admin.site.register(Page, PageAdmin)