from django.db import models

# Create your models here.
class Data(models.Model):
    Date = models.DateField()
    PM10 = models.IntegerField()
    NO2 = models.IntegerField()
    SO2 = models.IntegerField()
    O3 = models.IntegerField()
    AQI = models.IntegerField()


class Data_Predicted(models.Model):
    Date = models.DateField()
    PM10 = models.IntegerField()
    NO2 = models.IntegerField()
    SO2 = models.IntegerField()
    O3 = models.IntegerField()
    AQI = models.IntegerField()

class Update(models.Model):
    dat_up = models.IntegerField()