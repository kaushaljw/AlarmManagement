

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

time_date = ['ALARM_TIME','CANCEL_TIME','ACK_TIME','EVENT_TIME','INSERT_TIME','UPDATE_TIMESTAMP','TERMINATED_TIME']
data2 = pd.read_csv("C:/Users/jhunjhun/Documents/alarmDump/a4ossv04_fm_dump/fm_alarms_18012019_085951.csv"
                    , parse_dates=time_date
                    )

data2 = data2.drop(['TROUBLE_TICKET_ID','EXTRA_TEXT','USER_ADDITIONAL_INFO','DIAGNOSTIC_INFO','ADDITIONAL_TEXT5','ADDITIONAL_TEXT6','ADDITIONAL_TEXT7','CORRELATED_ALARM','CORRELATING_ALARM','CORRELATOR_CREATED','DELETED_BY','NOTES_INDICATOR'],axis=1) 

def handle_non_numerical_data(data2):
#    columns = data2.columns.values
    columns = ['DN','CANCELLED_BY','ACKED_BY','SUPPLEMENTARY_INFO','OC_ID','ORIGINAL_DN','LIFTED_DN','AGENT_ID']
    for column in columns:
        text_digit_vals={}
        def convert_to_int(val):
            return text_digit_vals[val]
        
        if data2[column].dtype != np.int64 and data2[column].dtype != np.float64:
            column_contents = data2[column].values.tolist()
            unique_elements = set(column_contents)
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals :
                    text_digit_vals[unique] = x
                    x+=1
                    
            data2[column] = list(map(convert_to_int,data2[column]))
            
    return data2

data2 = handle_non_numerical_data(data2) 

