
'''
This program is a tool to analyse severity based on the alarm_time, termination_time and agent_id
It does the analysis by removing AUTOACK from ACKED_BY 
1. First it will ask to provide path where the file is present.
2. It will ask to provide the file name to be analysed.
3. Provide the SEVERITY to be analysed.
It will provide the AGENT_ID based on the number of appearances
Than the time difference between TERMINATED_TIME and AGENT_ID
And finally the graph between the dates and the time difference in seconds
4. It will ask to provide AGENT_ID based on which the analysis is to be done.
5. Than the severity.
6. It will provide output in the same way as given above
'''




#C:\Users\jhunjhun\Documents\alarmDump\a4ossv04_fm_dump\fm_alarms_18012019_085951.csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

time_date = ['ALARM_TIME','CANCEL_TIME','ACK_TIME','EVENT_TIME','INSERT_TIME','UPDATE_TIMESTAMP','TERMINATED_TIME']
filepath = input("Enter the path where file is saved : ")
filename = input("Enter the file name: ")
file = filepath + "\\" + filename
dataset1 = pd.read_csv(file
#                    , parse_dates=time_date,index_col=0
                    )

dataset1['ALARM_TIME'] = pd.to_datetime(dataset1['ALARM_TIME'], dayfirst = True)
dataset1['CANCEL_TIME'] = pd.to_datetime(dataset1['CANCEL_TIME'], dayfirst = True)

file1 = filepath + "fm_alarms1.csv"

dataset1.to_csv(file1)

dataset2 = pd.read_csv(file1
                    , parse_dates=time_date,index_col=0
                    )
dataset2 = dataset2.iloc[0:6952]
dataset2['TERMINATED_TIME'] = pd.to_datetime(dataset2['TERMINATED_TIME'], dayfirst = True)

sev = input("Enter the severity: ")
severity = int(sev)
dataset3 = dataset2[dataset2.ACKED_BY != 'AUTOACK']
ax = plt.subplot2grid((1,1),(0,0))
 
for label in ax.xaxis.get_ticklabels():
    label.set_rotation(45)
dataset3 = dataset3[dataset3["CANCEL_TIME"].notnull()]
dataset3 = dataset3[dataset3["SEVERITY"].notnull()]
dataset3 = dataset3[dataset3.SEVERITY == severity]
dataset3 = dataset3.sort_values('ALARM_TIME')

print(dataset3.groupby(['AGENT_ID']).size().sort_values(ascending=False))


dataset3['DIFF'] = dataset3['TERMINATED_TIME'] - dataset3['ALARM_TIME']
print(dataset3[['ALARM_TIME','DIFF']])
dataset3['DIFF'] = dataset3['DIFF'].dt.total_seconds()
plt.plot(dataset3.ALARM_TIME,dataset3.DIFF)
plt.title('Time analysis')
plt.xlabel('Date')
plt.ylabel('Time Difference (in seconds)')
plt.legend()
plt.show()

agentid = input("Enter the agent_id: ")
dataset4 = dataset2[dataset2.AGENT_ID == agentid]
dataset4 = dataset4[dataset4.ACKED_BY != 'AUTOACK']
sev = input("Enter the severity: ")
severity = int(sev)
dataset4 = dataset4[dataset4["CANCEL_TIME"].notnull()]
dataset4 = dataset4[dataset4["SEVERITY"].notnull()]
dataset4 = dataset4[dataset4.SEVERITY == severity]
dataset4 = dataset4.sort_values('ALARM_TIME')
ax = plt.subplot2grid((1,1),(0,0))
 
for label in ax.xaxis.get_ticklabels():
    label.set_rotation(45)

dataset4 = dataset4[dataset4["CANCEL_TIME"].notnull()]
dataset4 = dataset4[dataset4["SEVERITY"].notnull()]
dataset4 = dataset4[dataset4.SEVERITY == severity]
dataset4 = dataset4.sort_values('ALARM_TIME')

dataset4['DIFF'] = dataset4['TERMINATED_TIME'] - dataset4['ALARM_TIME']
print(dataset4[['ALARM_TIME','DIFF']])
dataset4['DIFF'] = dataset4['DIFF'].dt.total_seconds()
plt.plot(dataset4.ALARM_TIME,dataset4.DIFF)
plt.title('Time analysis')
plt.xlabel('Date')
plt.ylabel('Time Difference (in seconds)')
plt.legend()
plt.show()
