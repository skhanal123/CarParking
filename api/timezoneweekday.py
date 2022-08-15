'''
This file contains the details and functions to convert the iso-date passed by user as query parameters

'''''

# The complete list of dictionary with "isoweekday" as key and "weekday" as value
weekday = {
    "1":"mon",
    "2":"tues",
    "3":"wed",
    "4":"thurs",
    "5":"fri",
    "6":"sat",
    "7":"sun"
}

# The following function helps to find the weekday based on the "isoweekday"
def findweekday(x):
    return weekday.get(x)



# The complete list of timezones can be added to the following dictionary
# For this project, I have only included two timezones
timezone = {
    "-05:00":"America/Chicago",
    "-04:00":"America/Toronto",
}

# The following function helps to find the timezone name based on the "utcoffset"
def findtimezone(x):
    return timezone.get(x)