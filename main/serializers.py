from rest_framework import fields, serializers
from .models import Data_Predicted

class DataPredSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('Date','PM10','NO2','SO2','O3','AQI')
        model = Data_Predicted
