from atexit import register
from django import template #para crear tags para mas paginas o las que se vayan creando 
from pages.models import Page

register = template.Library()

@register.simple_tag #se transforma la funcion en un simple tag y se registra en la libreria de templates
def get_page_list():
    pages = Page.objects.all()
    return pages