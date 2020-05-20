import pandas as pd

def trimTimeFrame(dataFrame, startDate, endDate):
    """
    Returns a cropped data frame to between the given dates in the format of:
    YYYY-MM-DD hh:mm:ss
    """
    return dataFrame[startDate, endDate]