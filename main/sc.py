import requests
from datetime import datetime

aq = []
def scrap():
    url = "http://vc8006.pythonanywhere.com/api/"
    response = requests.request("GET", url)

    r = response.json()
    for i in range(1,31):
        aq.append(r[-i]['AQI'])
        # print(r[-i])
        
    # print(response.text)
    print(aq)

scrap()