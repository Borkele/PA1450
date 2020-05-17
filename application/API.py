import requests
import pandas as pd
from datetime import datetime

def getAPIJson(timeFrame):
    """
    Returns a pandas tempratuere dataframe from SMHI
    Inputs:
    hour: Returns data from the last h
    day: Returns data from the last 24 h
    month: Returns data from the last 3 months

    """
    if (timeFrame != ''):
        if (timeFrame == 'day'):
            api = requests.get('https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1/station/65090/period/latest-day/data.json')
        
        elif (timeFrame == 'month'):
            api = requests.get('https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1/station/65090/period/latest-months/data.json')
        
        elif (timeFrame == 'hour'):
            api = requests.get('https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1/station/65090/period/latest-hour/data.json')
        
        if (api.status_code() == 200):
            lst = api.json()

            dataFrame = pd.DataFrame(lst["value"])

            date_df = pd.to_datetime(dataFrame['date'], unit='ms')
            value_df = pd.to_numeric(dataFrame['value'])

            dataFrame['date'] = date_df
            dataFrame['value'] = value_df
            return dataFrame
