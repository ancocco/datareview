# datareview
python files and data review
unempolymentrate file loads a csv file about the US unemployment rate
aggregationpivotbl file uses groupby and data aggregation in pivot_table

plotdailymeanpm25pm10 reads a csv file containing pm2.5 and pm10 values, cleans the data from Nan and 0 values. It calculates the daily average of the 
pm2.5 and pm10 recordings. It plots the mean values after interpolating dta to get rid of NaN data produced by the resampling. The same code can be modified to calculate min, max, std, median.

