import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from .models import Data , Data_Predicted ,Update
from datetime import date
import datetime
import statsmodels.api as sm
from pandas.tseries.offsets import DateOffset

# df = pd.read_csv("./main/static/new_data.csv",parse_dates = ['Date'], index_col = ['Date'])
update = Update()
data1 = Data_Predicted()
data = Data()
q = Data.objects.all().values()
df = pd.DataFrame(q)
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index(df['Date']) 

m = Data_Predicted.objects.all().values()
df_pred = pd.DataFrame(m)
df_pred['Date'] = pd.to_datetime(df_pred['Date'])
df_pred = df_pred.set_index(df_pred['Date']) 

from sklearn.metrics import mean_squared_error
import statsmodels.graphics.tsaplots as sgt

from statsmodels.tsa.arima_model import ARIMA
df = df_pred
size =  int(len(df)*0.8)
df_train = df.iloc[:size]
df_test = df.iloc[size:]

# u = Update.objects.get(name = "")
u = Update.objects.all().values()

date1 = [2555]
date2 = [2556]
def fun(df):
    dfa = df['AQI']
    df = df.dropna()
    future_dates = [df_pred.index[-1] + DateOffset(days = x)for x in range(2)]
    future_datest_df_new = pd.DataFrame(index = future_dates[1:],columns=df.columns)

    my_order = (0, 0, 0)
    my_seasonal_order = (1, 0, 1, 12)
    smodel = sm.tsa.SARIMAX(dfa, order=my_order,seasonal_order=my_seasonal_order,trend= 't')
    result_seasonal = smodel.fit()
    # date1 = future_dates[0].date()
    # date2 = future_dates[1].date()
    predictions_seasonal = result_seasonal.predict(steps = 1)
    # predictions_seasonal = result_seasonal.predict(start=date1[0],end=date2[0],typ="levels")
    # predictions_seasonal = result_seasonal.forecast(steps = 1)[0]
    # data1.AQI = 20
    print('############################ f_date',future_dates[0].date())
    print('############################ future dates',future_dates)
    x_date_n = ""
    x_date_n = future_dates[0].date().strftime("%Y-%m-%d")
    print(x_date_n)
    print('AQI       :*********************** ',predictions_seasonal)
    data1.AQI = predictions_seasonal.iloc[-1]
    # data.AQI = predictions_seasonal.iloc[-1]

    # date1[0] = date1[0] + 1
    # date2[0] = date2[0] + 1

    # model = ARIMA(df_train['AQI'],order = (2,1,2))
    # model_fit = model.fit()
    # data1.AQI = model_fit.forecast(steps = 1)[0]
    # future_datest_df_new['AQI'] = model_fit.forecast(steps = 1)[0]

    smodel_so2 = sm.tsa.SARIMAX(df['SO2'], order=my_order,seasonal_order=my_seasonal_order,trend= 't')
    result_seasonal_so2 = smodel_so2.fit()
    predictions_seasonal_so2 = result_seasonal_so2.predict(steps = 1)
    # predictions_seasonal_so2 = result_seasonal_so2.forecast(steps = 1)[0]
    print('so2      : ',predictions_seasonal_so2.iloc[-1])
    data1.SO2 = predictions_seasonal_so2.iloc[-1]
    # data.SO2 = predictions_seasonal_so2.iloc[-1]
    # data1.SO2 = 20

    # model = ARIMA(df_train['SO2'],order = (2,1,2))
    # model_fit = model.fit()
    # # data1.SO2 = model_fit.forecast(steps = 1)[0]
    # # future_datest_df_new['SO2'] = model_fit.forecast(steps = 1)[0]
    # data1.SO2 = 20


    smodel_no2 = sm.tsa.SARIMAX(df['NO2'], order=my_order,seasonal_order=my_seasonal_order,trend= 't')
    result_seasonal_no2 = smodel_no2.fit()
    predictions_seasonal_no2 = result_seasonal_no2.predict(steps = 1)
    # predictions_seasonal_no2 = result_seasonal_no2.forecast(steps = 1)[0]
    print('no2        : ',predictions_seasonal_no2.iloc[-1])
    data1.NO2 = predictions_seasonal_no2.iloc[-1]
    # data.NO2 = predictions_seasonal_no2.iloc[-1]
    # data1.NO2 = 20

    # model = ARIMA(df_train['NO2'],order = (2,1,2))
    # model_fit = model.fit()
    # data1.NO2 = model_fit.forecast(steps = 1)[0]
    # future_datest_df_new['NO2'] = model_fit.forecast(steps = 1)[0]
    # data1.NO2 = model_fit.forecast(steps = 1)[0]

    smodel_o3 = sm.tsa.SARIMAX(df['O3'], order=my_order,seasonal_order=my_seasonal_order,trend= 't')
    result_seasonal_o3 = smodel_o3.fit()
    predictions_seasonal_o3 = result_seasonal_o3.predict(steps = 1)
    # predictions_seasonal_o3 = result_seasonal_o3.forecast(steps = 1)[0]
    print('o3        : ',predictions_seasonal_o3.iloc[-1])
    data1.O3 = predictions_seasonal_o3.iloc[-1]
    # data.O3 = predictions_seasonal_o3.iloc[-1]
    # data1.O3 = 20

    # model = ARIMA(df_train['O3'],order = (2,1,2))
    # model_fit = model.fit()
    # # data1.O3 = model_fit.forecast(steps = 1)[0]
    # # future_datest_df_new['O3'] = model_fit.forecast(steps = 1)[0]
    # data1.O3 = 80


    smodel_pm10 = sm.tsa.SARIMAX(df['PM10'], order=my_order,seasonal_order=my_seasonal_order,trend= 't')
    result_seasonal_pm10 = smodel_pm10.fit()
    predictions_seasonal_pm10 = result_seasonal_pm10.predict(steps = 1)
    # predictions_seasonal_pm10 = result_seasonal_pm10.forecast(steps = 1)[0]
    print('pm10       : ',predictions_seasonal_pm10.iloc[-1])
    data1.PM10 = predictions_seasonal_pm10.iloc[-1]
    # data.PM10 = predictions_seasonal_pm10.iloc[-1]
    # data1.PM10 = 20

    # model = ARIMA(df_train['PM10'],order = (2,1,2))
    # model_fit = model.fit()
    # data1.PM10 = model_fit.forecast(steps = 1)[0]
    # future_datest_df_new['PM10'] = model_fit.forecast(steps = 1)[0]
    # data1.PM10 = model_fit.forecast(steps = 1)[0]


    # df = pd.concat([df,future_datest_df_new])
    # print(df.tail())
    # data1.Date = future_dates[1].strftime('%Y-%m-%d')
    data1.Date = pd.to_datetime(future_dates[1]).date()
    # data.Date = pd.to_datetime(future_dates[1]).date()
    data1.save()
    # data.save()
    # print(future_dates[1].strftime('%Y-%m-%d'))
    # print(future_datest_df_new['AQI'])
    # return df




d1 = df['AQI'][-30:].tolist()
d2 = df.index[-30:].strftime('%Y-%m-%d').tolist()

d3 = df['SO2'][-30:].tolist()
d4 = df['NO2'][-30:].tolist()
d5 = df['O3'][-30:].tolist()

print(df['Date'])
print(df.tail())
