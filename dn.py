'''
DN = “PLMN-CBIS/CBIS-PCRFSPS1-NOR/COMPUTE-overcloud-ovscompute-23/SERVER-1”
After removing ‘AUTOACK’ from ACKED_BY it was found that: -
1.	ORIGINAL_SEVERITY is always 99.
2.	SEVERITY is always 1.
3.	Time difference between TERMINATED_TIME and ALARM_TIME is between 1 day and 1 day 2 hours.

'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

time_date = ['ALARM_TIME','CANCEL_TIME','ACK_TIME','EVENT_TIME','INSERT_TIME','UPDATE_TIMESTAMP','TERMINATED_TIME']

dataset1 = pd.read_csv("C:/Users/jhunjhun/Documents/alarmDump/a4ossv04_fm_dump/fm_alarms_18012019_085951.csv"
#                    , parse_dates=time_date,index_col=0
                    )

dataset1['ALARM_TIME'] = pd.to_datetime(dataset1['ALARM_TIME'], dayfirst = True)
dataset1['CANCEL_TIME'] = pd.to_datetime(dataset1['CANCEL_TIME'], dayfirst = True)
#dataset1['TERMINATED_TIME'] = pd.to_datetime(dataset1['TERMINATED_TIME'], dayfirst = True)

dataset1.to_csv("C:/Users/jhunjhun/Documents/alarmDump/a4ossv04_fm_dump/fm_alarms1.csv")

dataset2 = pd.read_csv("C:/Users/jhunjhun/Documents/alarmDump/a4ossv04_fm_dump/fm_alarms1.csv"
                    , parse_dates=time_date,index_col=0
                    )
                    
#removing ACKED_BY = 'AUTOACK'                    
dataset5 = dataset2[dataset2.ACKED_BY != 'AUTOACK']

#For perticular DN
dataset5 = dataset5[dataset5.DN == 'PLMN-CBIS/CBIS-PCRFSPS1-NOR/COMPUTE-overcloud-ovscompute-23/SERVER-1']
dataset5['TERMINATED_TIME'] = pd.to_datetime(dataset5['TERMINATED_TIME'], dayfirst = True)
ax = plt.subplot2grid((1,1),(0,0))
 
for label in ax.xaxis.get_ticklabels():
    label.set_rotation(45)
dataset5 = dataset5[dataset5["CANCEL_TIME"].notnull()]
dataset5 = dataset5[dataset5["SEVERITY"].notnull()]
dataset5 = dataset5.sort_values('CONSEC_NBR')
dataset5['DIFF'] = dataset5['TERMINATED_TIME'] - dataset5['ALARM_TIME']
dataset5['DIFF'] = dataset5['DIFF'].dt.total_seconds()
plt.plot(dataset5.CONSEC_NBR,dataset5.DIFF)

