import pandas as pd
import datetime
from dateutil.parser import parse

def trimTimeFrame(dataFrame, startDate, endDate):
    """
    Returns a cropped data frame to between the given dates in the format of:
    YYYY-MM-DD hh:mm:ss
    """
    return dataFrame[startDate : endDate]


def translateDateFormat(inputDate):
    """ Translates a date into the YYYY-MM-DD format."""
    original = parse(inputDate)
    return original.strftime('%Y-%m-%d')

def getWeekdayIndex(weekday):
    if weekday == "monday":
        return 0
    if weekday == "tuesday":
        return 1
    if weekday == "wednesday":
        return 2
    if weekday == "thursday":
        return 3
    if weekday == "friday":
        return 4
    if weekday == "saturday":
        return 5
    if weekday == "sunday":
        return 6