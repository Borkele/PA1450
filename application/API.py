import requests
import pandas as pd
from datetime import datetime

def getAPIJson(timeFrame, dataType):
    """
    Returns a pandas tempratuere dataframe from SMHI
    Inputs:
    hour: Returns a string of the last h temprature
    day: Returns data from the last 24 h
    month: Returns data from the last 3 months

    """
    if (dataType != ''):
        if (dataType == 'temperature'):
            if (timeFrame != ''):
                if (timeFrame == 'day'):
                    api = requests.get('https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1/station/65090/period/latest-day/data.json')
                
                elif (timeFrame == 'month'):
                    api = requests.get('https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1/station/65090/period/latest-months/data.json')
                
                elif (timeFrame == 'hour'):
                    api = requests.get('https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1/station/65090/period/latest-hour/data.json')

                    lst = api.json()

                    lst2 = lst['value'].pop()

                    return lst2['value']

                lst = api.json()

                dataFrame = pd.DataFrame(lst["value"])

                date_df = pd.to_datetime(dataFrame['date'], unit='ms')
                value_df = pd.to_numeric(dataFrame['value'])

                dataFrame['date'] = date_df
                dataFrame['value'] = value_df
                dataFrame.set_index(['date'], inplace=True)

                return dataFrame

        else:
            return False
    else: 
        return False
