import pandas as pd
import datetime
import matplotlib.pyplot as plt
from dictionarywtime import months
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
    #Iterate the months of the year
    for m in clean_data['date'].dt.month.drop_duplicates():
        #Construct time string interval that includes year and month
        yyyy_m = str(y) + "-" + str(m)
        #Use time string to select from index date the right month
        month_data = nozero_data.loc[yyyy_m, ["pm25","pm10"]]
        #Create dataframe containing daily mean values for a month: use of resample.
        #The data for missing values are interpolated to the nearest
        cmonth_data = month_data.resample("D").mean().interpolate("nearest")
        #Plot the data
        cmonth_data.plot()
        #Take care of ticks, labes,box, legend and title. The month names are loaded from a dictionary
        plt.title("PM2.5, PM10: mean values - " + months[m] + " 2019, New Delhi",color='#545') #Title PM2.5, PM10: mean, max, min
        plt.tick_params(bottom=False, top=False, left=False) #remove the ticks
        plt.ylabel('PM2.5, PM10 mean values - micrograms/cubicmeter', c="g")
        plt.xlabel("Daily mean values give an idea of the trend over a longer period of time", c="g")
        plt.grid(color = '#ddd', linestyle = 'dashdot',linewidth = 0.5)
        #It makes borders disappear
        plt.box(False)
        plt.legend(framealpha=1, frameon=False)
        plt.show()
        