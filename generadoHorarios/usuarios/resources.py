from import_export import resources
from .models import User,Coordina,Docente

class UserResources(resources.ModelResource):
    class meta:
        model = User

class CoordinaResources(resources.ModelResource):
    class meta:
        model = Coordina
        
class DocenteResources(resources.ModelResource):
    class meta:
        model = Docente