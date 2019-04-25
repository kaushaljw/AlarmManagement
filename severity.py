'''
Code to compare severity with both alarm time and cancel time
'''

#For all data

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

time_date = ['ALARM_TIME','CANCEL_TIME','ACK_TIME','EVENT_TIME','INSERT_TIME','UPDATE_TIMESTAMP','TERMINATED_TIME']

dataset1 = pd.read_csv("C:/Users/jhunjhun/Documents/alarmDump/a4ossv04_fm_dump/fm_alarms_18012019_085951.csv"
#                    , parse_dates=time_date,index_col=0
                    )

dataset1['ALARM_TIME'] = pd.to_datetime(dataset1['ALARM_TIME'], dayfirst = True)
dataset1['CANCEL_TIME'] = pd.to_datetime(dataset1['CANCEL_TIME'], dayfirst = True)

dataset1.to_csv("C:/Users/jhunjhun/Documents/alarmDump/a4ossv04_fm_dump/fm_alarms1.csv")

dataset2 = pd.read_csv("C:/Users/jhunjhun/Documents/alarmDump/a4ossv04_fm_dump/fm_alarms1.csv"
                    , parse_dates=time_date,index_col=0
                    )
                    
ax = plt.subplot2grid((1,1),(0,0))
 
for label in ax.xaxis.get_ticklabels():
    label.set_rotation(45)
dataset2 = dataset2[dataset2["CANCEL_TIME"].notnull()]
dataset2 = dataset2[dataset2["SEVERITY"].notnull()]
dataset2 = dataset2.sort_values('SEVERITY')
plt.plot(dataset2.SEVERITY,dataset2.ALARM_TIME, linewidth=3.0)
dataset2 = dataset2.sort_values('SEVERITY')
plt.plot(dataset2.SEVERITY,dataset2.CANCEL_TIME)
plt.title('Severity')
plt.xlabel('Severity')
plt.ylabel('Alarm Time and Cancel Time')
plt.legend()
plt.show()

#For DN = PLMN-PLMN/NAFD-6

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

time_date = ['ALARM_TIME','CANCEL_TIME','ACK_TIME','EVENT_TIME','INSERT_TIME','UPDATE_TIMESTAMP','TERMINATED_TIME']

dataset1 = pd.read_csv("C:/Users/jhunjhun/Documents/alarmDump/a4ossv04_fm_dump/fm_alarms_18012019_085951.csv"
#                    , parse_dates=time_date,index_col=0
                    )

dataset1['ALARM_TIME'] = pd.to_datetime(dataset1['ALARM_TIME'], dayfirst = True)
dataset1['CANCEL_TIME'] = pd.to_datetime(dataset1['CANCEL_TIME'], dayfirst = True)

dataset1.to_csv("C:/Users/jhunjhun/Documents/alarmDump/a4ossv04_fm_dump/fm_alarms1.csv")

dataset2 = pd.read_csv("C:/Users/jhunjhun/Documents/alarmDump/a4ossv04_fm_dump/fm_alarms1.csv"
                    , parse_dates=time_date,index_col=0
                    )
dataset2 = dataset2[dataset2.DN == 'PLMN-PLMN/NAFD-6']
ax = plt.subplot2grid((1,1),(0,0))
 
for label in ax.xaxis.get_ticklabels():
    label.set_rotation(45)
dataset2 = dataset2[dataset2["CANCEL_TIME"].notnull()]
dataset2 = dataset2[dataset2["SEVERITY"].notnull()]
dataset2 = dataset2.sort_values('SEVERITY')
plt.plot(dataset2.SEVERITY,dataset2.ALARM_TIME, linewidth=3.0)
dataset2 = dataset2.sort_values('SEVERITY')
plt.plot(dataset2.SEVERITY,dataset2.CANCEL_TIME)
plt.title('Severity')
plt.xlabel('Severity')
plt.ylabel('Alarm Time and Cancel Time')
plt.legend()
plt.show()

