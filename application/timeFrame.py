import pandas as pd
import datetime
from dateutil.parser import parse

def trimTimeFrame(dataFrame, startDate, endDate):
    """
    Returns a cropped data frame to between the given dates in the format of:
    YYYY-MM-DD hh:mm:ss
    """
    return dataFrame[startDate, endDate]


def translateDateFormat(inputDate):
    """ Translates a date into the YYYY-MM-DD format."""
    original = parse(inputDate)
    return original.strftime('%Y-%m-%d')