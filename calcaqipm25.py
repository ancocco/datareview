import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from aqifunc import read_dict
from aqifunc import read10_dict
#DATA CSV LOADING
dehli_path = "C:\\Personale\\WebDes\\thonotes\\delhi\\apr_oct2019.csv"
raw_data = pd.read_csv(dehli_path)
#DATA CLEANING
#Clean date record from a alphabetical part ==== IST ===
raw_data["date"] = raw_data["created_at"].str.replace('IST', '')
#Convert date to datetime format 
raw_data["date"] = pd.to_datetime(raw_data["date"])
#Clean original data from NaN values
clean_data = raw_data.dropna(subset=["pm25","pm10"])
#Exclude values equal to zero
nozero_data = clean_data[clean_data["pm25"]!=0]
#Creating a SERIES that contains only date year  to iterate the year
pm_year = clean_data['date'].dt.year
for y in pm_year.drop_duplicates():
    #Set Index on date and be able to select datasets
    nozero_data.set_index("date", inplace=True)
    year_data = nozero_data.loc[str(y), ["pm25","pm10"]]
    #A daily pm2.5 measurements average is created
    pyear_data = year_data.resample("D").mean().interpolate("nearest")
    #CALCULATE AQI from aqi_func see extra py file
    run_aqi_calc = []
    run_aqi_air = []
    for i,row in pyear_data.iterrows():
        aqi_v, aqi_air = read_dict(row["pm25"])
        run_aqi_calc.append(aqi_v)
        run_aqi_air.append(aqi_air)
    #A new column for AQI values is created
    pyear_data["aqi25"] =  run_aqi_calc
    #A new column for AQI level of health concerns is created
    pyear_data["aqi25air"] = run_aqi_air
    #the days with the same level of health concern are counted and a mean aqi value is created
    day25_count = pyear_data.groupby("aqi25air")["aqi25"].agg(['mean','count'])
    #The AQI mean value is rounded to an integer
    day25_count['mean'] = day25_count['mean'].round().astype(int)
    #The index is resetted
    day25_count = day25_count.reset_index()
    #A new index to AQI mean is created, so, during the plot it deploys automatically on the y axis
    day25_count.set_index('mean', inplace=True)
    #The count of days is sorted to appear from the top less numerous to the bottom, more numerous
    day25_count = day25_count.sort_values('count',ascending=False)
    #It starts the plot preparation
    day25_count.plot(kind="barh", legend=None)
    plt.tick_params(bottom=False, top=False, left=False) #remove the ticks
    plt.title("Number of days grouped by levels of health concern from April\nto October 2019: Air Quality Index based on PM10 measurements", loc="left", color="grey")
    plt.text(x=2, y=4, s="1 VERY UNHEALTHY DAY, 221 AS MEAN AQI", color="#880000", fontsize=10.0, fontweight='bold')
    plt.text(x=5, y=3, s="4 GOOD DAYS AND 42 AS MEAN AQI", color="green", fontsize=10.0, fontweight='bold')
    plt.text(x=30, y=2, s="28 UNHEALTHY DAYS, 160 AS MEAN AQI", color="#BB0000", fontsize=10.0, fontweight='bold')
    plt.text(x=62, y=0.7, s="61 UNHEALTHY DAYS\nFOR SENSITIVE GROUPS,\n120 AS MEAN AQI", color="#FF0000", fontsize=10.0, fontweight='bold')
    plt.text(x=1, y=0, s="97 DAYS OF MODERATE AIR AND AN AVERAGE AQI OF 73", color="orange", fontsize=10.0, fontweight='bold')
    plt.xlabel("Number of days", c="g")
    plt.ylabel("Mean AQI", c="g")
    plt.grid(color = '#ddd', linestyle = 'dashdot',linewidth = 0.5)
    #It makes borders disappear
    plt.box(False)
    plt.show()