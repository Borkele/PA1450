import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def generateGraph(dataFrame, timeFrame, dataType, name):
    """
    Takes a given pandas dataframe and converts it to a graph and saves it to the graphs folder.
    dataFrame: Converts the entire given data frame to a graph
    timeFrame: The dates/time to show on the x axies

    dataType inputs:
    temperature
    precipitation
    wind
    sight
    pressure
    """  
    
    fig, ax = plt.subplots(figsize=(15,15))

    if (timeFrame != ''):
        if (timeFrame == 'month'):
            fig, ax = plt.subplots()
            ax.plot(dataFrame.index, dataFrame['value'])
            ax.xaxis.set_major_locator(mdates.MonthLocator())
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
            ax.xaxis.grid(True)
            ax.yaxis.grid(True)
            ax.xaxis.set_minor_locator(mdates.WeekdayLocator())
            fig.set_size_inches(18, 5)
            fig.autofmt_xdate()
        
        elif (timeFrame == 'day'):
            fig, ax = plt.subplots()
            ax.plot(dataFrame.index, dataFrame['value'])
            ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:00'))
            ax.xaxis.grid(True)
            ax.yaxis.grid(True)
            ax.xaxis.set_minor_locator(mdates.HourLocator())
            fig.set_size_inches(8, 5)
            fig.autofmt_xdate()

        try:
            if (dataType == 'temperature'):
                ax.set_title("Temperature in °C")
            elif (dataType == 'precipitation'):
                ax.set_title("precipitation in mm")
            elif (dataType == 'wind'):
                ax.set_title("wind in m/s")
            elif (dataType == 'sight'):
                ax.set_title("sight in meters")
            elif (dataType == 'pressure'):
                ax.set_title("pressure in hectopascal")
            else:
                return False

            fig.savefig(f"static/image/graphs/{name}.png", bbox_inches='tight')
            return True

        except Exception:
            return False  
                  
        else:
            return False
    else: 
        return False