from datetime import datetime


def timeConversion(s):

    # Parse string to datetime object
    dt = datetime.strptime(s, "%I:%M:%S%p")

    # Format the datetime object as military time
    military_time_str = dt.strftime("%H:%M:%S")


    return military_time_str



timeConversion("07:05:45PM")

# %I is used to parse the hour into 12 hour format
# %M is used to parse the minute


