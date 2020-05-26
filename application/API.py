import requests
import pandas as pd
from datetime import datetime
import xml.etree.ElementTree as ET


def getAPIJson(timeFrame, dataType, forecast = False):
    """
    Returns a pandas tempratuere dataframe from SMHI
    timeFrame inputs:
    hour: Returns a string of the last h temprature
    day: Returns data from the last 24 h
    month: Returns data from the last 3 months

    dataType inputs:
    temperature: retruns celsius/h
    precipitation: returns precipitation/h in mm
    wind: retruns wind avrage/h
    sight: returns sight in meter every h
    pressure: sea presure/h


    """
    if (forecast == False):
        if (dataType != ''):
            if (dataType == 'temperature'):
                parameter = '1'
            elif (dataType == 'precipitation'):
                parameter = '7'
            elif (dataType == 'wind'):
                parameter = '4'
            elif (dataType == 'sight'):
                parameter = '12'
            elif (dataType == 'pressure'):
                parameter = '9'
            else:
                return False

            if (timeFrame != ''):
                if (timeFrame == 'day'):
                    timeFrameValue = 'latest-day'
                    
                elif (timeFrame == 'month'):
                    timeFrameValue = 'latest-months'
                
                elif (timeFrame == 'hour'):
                    api = requests.get(f'https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/{parameter}/station/65090/period/latest-hour/data.json')

                    lst = api.json()

                    lst2 = lst['value'].pop()

                    return lst2['value']

                api = requests.get(f'https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/{parameter}/station/65090/period/{timeFrameValue}/data.json')

                lst = api.json()

                dataFrame = pd.DataFrame(lst['value'])

                dateDf = pd.to_datetime(dataFrame['date'], unit='ms')
                valueDf = pd.to_numeric(dataFrame['value'])

                dataFrame['date'] = dateDf
                dataFrame['value'] = valueDf
                dataFrame.set_index(['date'], inplace=True)

                return dataFrame

            else:
                return False
        else: 
            return False
    else:
        api = requests.get('http://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/15/lat/56/data.json')

        lst = api.json()

        data = []

        for time in lst["timeSeries"]:
    
            dict = {}
            dict['date'] = time['validTime']

            if dataType == "temperature":
                dict['value'] = float(time['parameters'][11]['values'][0])
            elif dataType == 'precipitation':
                dict['value'] = float(time['parameters'][3]['values'][0])
            elif dataType == 'wind':
                dict['value'] = float(time['parameters'][14]['values'][0])
            elif dataType == 'pressure':
                dict['value'] = float(time['parameters'][10]['values'][0])

            data.append(dict)

        dataFrame = pd.DataFrame(data)

        dateDf = pd.to_datetime(dataFrame['date'], format = '%Y-%m-%dT%H:%M:%SZ')
        valueDf = pd.to_numeric(dataFrame['value'])

        dataFrame['date'] = dateDf
        dataFrame['value'] = valueDf
        dataFrame.set_index(['date'], inplace=True)

        return dataFrame



def getAPIXML(data_type):
    """Returns a pandas tempratuere dataframe from yr.no
    
        dataType inputs:
        temperature: retruns celsius/h
        precipitation: returns precipitation/h in mm
        wind: retruns wind avrage/h
        pressure: sea presure/h
    """

    #handles xml like a tree
    tree = ET.fromstring(requests.get('http://www.yr.no/place/Sweden/Blekinge/Karlskrona/forecast.xml').text)
    #root = tree.getroot()
    print(tree.tag)
    data = []
    for time in tree.iter('time'):
        start_date = time.attrib['from']
        #end_date = time.attrib['to']
        
        dict = {}
        dict['date'] = start_date
        if data_type == "temperature":
            temp = float(time[4].attrib['value'])
            dict['value'] = temp
        elif data_type == 'precipitation':
            precipitation_value = float(time[1].attrib['value'])
            dict['value'] = precipitation_value
        elif data_type == 'wind':
            wind_speed = float(time[3].attirb['mps']) # meter per second
            dict['value'] = wind_speed
        elif data_type == 'pressure':
            pressure = float(time[5].attrib['value'])
            dict['value'] = pressure
        else:  
            return False
        data.append(dict)

    dataFrame = pd.DataFrame(data)

    #kolla med anton om vad fan ms är för det skedde en type error, måste det vara en integer ellet nåt sånt?

    dateDf = pd.to_datetime(dataFrame['date'], format = '%Y-%m-%dT%H:%M:%S')

    valueDf = pd.to_numeric(dataFrame['value'])

    dataFrame['date'] = dateDf
    dataFrame['value'] = valueDf
    dataFrame.set_index(['date'], inplace=True)

    dataFrame = dataFrame.head(12)
    return dataFrame
