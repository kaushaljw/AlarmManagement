
#CODE TO CREATE PANDAS PROFILING FOR THE DATASET

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

#CONVERTING STRING DATE TO THE TIMESTAMP
time_date = ['ALARM_TIME','CANCEL_TIME','ACK_TIME','EVENT_TIME','INSERT_TIME','UPDATE_TIMESTAMP','TERMINATED_TIME']
data2 = pd.read_csv("C:/Users/jhunjhun/Documents/alarmDump/a4ossv04_fm_dump/fm_alarms_18012019_085951.csv"
                    , parse_dates=time_date
                    )

data2 = data2.drop(['TROUBLE_TICKET_ID','EXTRA_TEXT','USER_ADDITIONAL_INFO','DIAGNOSTIC_INFO','ADDITIONAL_TEXT5','ADDITIONAL_TEXT6','ADDITIONAL_TEXT7','CORRELATED_ALARM','CORRELATING_ALARM','CORRELATOR_CREATED','DELETED_BY','NOTES_INDICATOR'],axis=1) 

#Display of Pandas Profiling 

import pandas_profiling
profile = pandas_profiling.ProfileReport(data2)
display(profile)
profile.to_file(outputfile="C:/Users/jhunjhun/Desktop/myoutputfile.html")
