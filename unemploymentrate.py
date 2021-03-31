import csv
import matplotlib.pyplot as plt
#Use pandas and dataframe
import pandas as pd

path = 'C:\\Personale\\WebDes\\thonotes\\noemploymrate.csv'
unrate = pd.read_csv(path)
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
print(unrate.head(12))
date_1948 = unrate["DATE"].head(12)
value_1948 = unrate["UNRATE"].head(12)
print(value_1948)
#By default, Matplotlib displays a coordinate grid with:
#the x-axis and y-axis values ranging from -0.06 to 0.06    no grid lines   no data
# The axis ticks consist of tick marks and tick labels
plt.plot(date_1948, value_1948)
plt.xticks(rotation=30)
plt.show()
#To create a line chart of the unemployment data from 1948, we need:
#       the x-axis to range from 01-01-1948 to 12-01-1948
#       the y-axis to range from 3.4 to 4.0
#       plt.plot(x_values, y_values)
#   Matplotlib will accept any iterable object, like NumPy arrays and pandas.Series instances.
#plt.plot(unrate["DATE"].head(12),unrate["VALUE"].head(12))
