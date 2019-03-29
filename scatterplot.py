
'''scatter.png

Scatter plot of all columns

'''


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("C:/Users/jhunjhun/Documents/alarmDump/a4ossv04_fm_dump/fm_alarms_18012019_085951.csv", parse_dates=['ALARM_TIME','CANCEL_TIME','ACK_TIME','EVENT_TIME','INSERT_TIME','UPDATE_TIMESTAMP','TERMINATED_TIME'])

data = data.drop(['TROUBLE_TICKET_ID','EXTRA_TEXT','USER_ADDITIONAL_INFO','DIAGNOSTIC_INFO','ADDITIONAL_TEXT5','ADDITIONAL_TEXT6','ADDITIONAL_TEXT7','CORRELATED_ALARM','CORRELATING_ALARM','CORRELATOR_CREATED','DELETED_BY','NOTES_INDICATOR'],axis=1)

sm = pd.plotting.scatter_matrix(data, figsize=(25,25))
plt.show()
