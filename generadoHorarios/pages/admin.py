from django.contrib import admin
from .models import Page
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
admin.site.register(Page,SimpleHistoryAdmin)