from import_export import resources
from .models import Alumno,Docente

class DocenteResource(resources.ModelResource):
    class Meta:
        model = Docente