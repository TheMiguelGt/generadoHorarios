from import_export import resources
from .models import User,Admin

class AdminResource(resources.ModelResource):
     class Meta:
         model = User
