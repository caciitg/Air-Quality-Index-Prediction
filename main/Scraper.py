import requests
from datetime import datetime
import pandas as pd
from .models import  Data,Data_Predicted

data = Data()
data1 = Data_Predicted()



def scrap():
    url = "https://api.ambeedata.com/latest/by-city"
    querystring = {"city":"Delhi"}
    headers = {
        'x-api-key': "mqoZ9hQjIi3ZqydD8W3lU7fGnXJ5ndJI44sAUusN",
        'Content-type': "application/json"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)

    r = response.json()

    data.NO2 = r['stations'][0]['NO2']
    data.O3 = r['stations'][0]['OZONE']
    data.SO2 = r['stations'][0]['SO2']
    data.PM10 = r['stations'][0]['PM10']
    data.AQI = r['stations'][0]['AQI']

    x = pd.to_datetime(r['stations'][0]['updatedAt'])
    data.Date = x.date()
    data.save()

    print('no2',r['stations'][0]['NO2'])
    print('o3',r['stations'][0]['OZONE'])
    print('so2',r['stations'][0]['SO2'])
    print('pm10',r['stations'][0]['PM10'])
    print('aqi',r['stations'][0]['AQI'])
    print('date',r['stations'][0]['updatedAt'])
    print('date type',type(r['stations'][0]['updatedAt']))
    


    print(type(response))
    print(type(r))

    print(r['message'])
    print(r['stations'][0]['OZONE'])

    print(response.text)

# scrap()