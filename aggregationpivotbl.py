import datetime
import csv
import matplotlib.pyplot as plt
import numpy as np
#Use pandas and dataframe
import pandas as pd
path = 'C:\\Personale\\WebDes\\qparticmatter\\qparticulate.csv'
qairtot = pd.read_csv(path)
qair = qairtot[qairtot['mont']==1]
ygrouped = qair.groupby(['year','mont','nday'])[['pm25','pm10']]
ypm_stats = ygrouped.agg([np.mean, np.max, np.min])
# plot data
fig, ax = plt.subplots(figsize=(9,5))
#pv_pm_stats = qair.pivot_table(['pm25','pm10'], ['year','mont','nday'], aggfunc=[np.min, np.max, np.mean], margins=True).plot(ax=ax)
#pv_pm_stats = qair.pivot_table(['pm25','pm10'], ['year','mont','nday'], aggfunc=[np.min, np.max], margins=True).plot(ax=ax)
#pv_pm_stats = qair.pivot_table(['pm25','pm10'], ['year','mont','nday'], aggfunc=[np.mean], margins=True).plot(ax=ax)
pv_pm_stats = qair.pivot_table(['pm25','pm10'], ['year','mont','nday','hour'], aggfunc=[np.max], margins=True).plot(ax=ax)

#ax.xaxis.tick_top()
ax.tick_params(bottom=False, top=False, left=False) #remove the ticks
#pv_pm_stats.plot(kind='line', title='PM2.5, PM10 in Qatar', xlim=(0,20), legend=True)
ax.set(ylabel='PM2.5, PM10 values');
ax.xaxis.label.set_color("grey")
ax.yaxis.label.set_color("grey")
#It makes borders disappear
for location in ['left', 'right', 'bottom', 'top']: #all borders
    ax.spines[location].set_visible(False)
ax.tick_params(axis='x', colors='grey') #grey x top values to deflect attention
ax.tick_params(axis='y', colors='grey') #grey x top values to deflect attention
ax.set_yticks([0, 25, 50, 75, 100, 150, 200, 300, 400, 500])
plt.title('PM2.5, PM10: mean, max, min',color='grey') #Title PM2.5, PM10: mean, max, min
plt.title('PM2.5, PM10: max and min',color='grey') #Title PM2.5, PM10: max and min
plt.title('PM2.5, PM10: mean value',color='grey') #Title PM2.5, PM10: mean
plt.title('PM2.5, PM10: mean and min value per hour',color='grey') #Title PM2.5, PM10: mean for each hour
plt.title('PM2.5, PM10: max values, January 2019',color='grey') #Title PM2.5, PM10: mean for each month

legend = plt.legend()
plt.setp(legend.get_texts(), color='grey')#change text color in legend
legend.get_frame().set_linewidth(0.0)#remove border from legend
ax.axhline(y=0, xmin=0.01, xmax=0.96, linewidth=1, c='grey', alpha=0.1)  #the middle vertical line
ax.axhline(y=25, xmin=0.04, xmax=0.94, linewidth=1, c='grey', alpha=0.2)  #the middle vertical line
ax.axhline(y=50, xmin=0.02, xmax=0.945, linewidth=1, c='grey', alpha=0.35)  #the middle vertical line
ax.axhline(y=75, xmin=0.04, xmax=0.94, linewidth=1, c='grey', alpha=0.2)  #the middle vertical line
ax.axhline(y=100, xmin=0.01, xmax=0.95, linewidth=1, c='grey', alpha=0.3)  #the middle vertical line
ax.axhline(y=150, xmin=0.02, xmax=0.945, linewidth=1, c='grey', alpha=0.2)  #the middle vertical line
ax.axhline(y=200, xmin=0.01, xmax=0.95, linewidth=1, c='grey', alpha=0.25)  #the middle horizontal line
#ax.axhline(y=300, xmin=0.01, xmax=0.95, linewidth=1, c='grey', alpha=0.12)  #the middle horizontal line
#ax.axhline(y=400, xmin=0.01, xmax=0.95, linewidth=1, c='grey', alpha=0.09)  #the middle horizontal line
#ax.axhline(y=500, xmin=0.01, xmax=0.95, linewidth=1, c='grey', alpha=0.05)  #the middle horizontal line
#ax.axvline(x='(2018, 10, 21)', ymin=0.045, ymax=1.5, c='grey', alpha=0.2)  #the middle vertical line

plt.xticks(rotation = 45)
plt.show()
