from import_export import resources
from .models import Data

class DataResources(resources.ModelResource):
    class Meta:
        model = Data