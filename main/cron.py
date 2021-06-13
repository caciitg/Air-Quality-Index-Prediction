from . import Ml_model as ml
from .models import  Data, Data_Predicted 
from . import Scraper as sc

data = Data()
data1 = Data_Predicted()
def my_scheduled_job():
    # Test.objects.create(name = "test")
    # data.AQI = 2
    # data.save()
    ml.fun(ml.df)
    sc.scrap()
    

    # ml.f_s(ml.df)
    # print("hhhhhhhhhhhhhhheeeeeeeeeeeeeellllllllll")  
    # python manage.py runserver