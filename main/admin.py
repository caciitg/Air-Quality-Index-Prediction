from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Data , Data_Predicted, Update

admin.site.register(Update)

@admin.register(Data)
class DataAdmin(ImportExportModelAdmin):
    list_display = ("Date","PM10","NO2","SO2","O3","AQI")
    pass

@admin.register(Data_Predicted)
class Data_PredictedAdmin(ImportExportModelAdmin):
    # list_display = ("Date","PM10","NO2","SO2","O3")
    list_display = ("Date","PM10","NO2","SO2","O3","AQI")
    pass