## About The Project: 

It is not an unknown fact that air pollution will endanger human health and life in big
cities, especially for the elderly and children. This is not an individual problem but a
global one.With cutting edge technology entering the world every moment, it is our duty
to think about the community as well, and henceforth integrate tech and people. Many
countries in the world have, therefore, made air pollution monitoring and control stations
in many cities.
PM2.5 refers to the mass per cubic meter of air of particles with a size (diameter)
generally less than 2.5 micrometers (μm). They’re essentially tiny particles in the air that
reduce visibility and cause the air to appear hazy when levels are elevated, thus
contributing to air pollution. In this project, different machine learning models have been
employed to detect PM2.5 levels based on a data set consisting of daily atmospheric
conditions.

## Approach:
1. We obtain the dataset containing AQI and air quality data at hourly and daily level
of various stations across multiple cities in India.(This data has been made
publicly available by the Central Pollution Control Board)
2. Dataset preprocessing/cleaning(maximising its information content) + Data
Visualization using Seaborn/Matplotlib
3. Using time series forecasting methods to predict AQI at any given time using models like Arima, Sarimax, etc.
4. Selecting the model with highest accuracy + Displaying predicted daily AQIs
5. Deploying the project on web using Django


![screenshot](aqi_ss.png)

