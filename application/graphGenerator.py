import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def generateGraph(dataFrame, timeFrame):
    """
    Takes a given pandas dataframe and converts it to a graph and saves it to the graphs folder.
    dataFrame: Converts the entire given data frame to a graph
    timeFrame: The dates/time to show on the x axies
    """
    dataFrame.set_index(['date'], inplace=True)

    fig, ax = plt.subplots(figsize=(15,15))

    if (timeFrame != ''):
        if (timeFrame == 'month'):
            try:
                ax.xaxis.set_major_locator(mdates.DayLocator())
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
                
                plot = dataFrame.plot()
                fig = plot.get_figure()
                fig.savefig(f"application/static/image/{timeFrame}.png")
                return True
            except Exception:
                return False            

        elif (timeFrame == 'day'):
            try:
                ax.xaxis.set_major_locator(mdates.DayLocator())
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%b-%d %H:%M'))

                plot = dataFrame.plot()
                fig = plot.get_figure()
                fig.savefig(f"application/static/image/{timeFrame}.png")
                return True
            except Exception:
                return False

    else: 
        return False