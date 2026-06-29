def timeConversion(s):
    period = s[-2:]
    hour = s[:2]
    if period == "AM":
        if hour == "12":
            hour = "00"
    else:
        if hour != "12":
            hour = int(hour)+12
            hour = str(hour)
            if len(hour) == 1:
                hour = "0"+hour
    return hour + s[2:-2]















print(timeConversion("02:01:00PM"))