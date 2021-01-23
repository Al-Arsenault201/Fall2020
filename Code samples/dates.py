def convert_date(date_as_string):

    month = int(date_as_string[0:2])
    day = int(date_as_string[2:4])
    year = int(date_as_string[4:])

    if month == 1:
        return day
    elif month == 2:
        return day + 31
    elif month == 3:
        return day + 59
    elif month == 4:
        return day + 90
    elif month == 5:
        return day + 120
    elif month == 6:
        return day + 151
    elif month == 7:
        return day + 181
    elif month == 8:
        return day + 212
    elif month == 9:
        return day + 243
    elif month == 10:
        return day + 273
    elif month == 11:
        return day + 304
    else:
        return day + 334


if __name__ == "__main__":
    s = input("enter a date in the form MMDDYYYY")
    d = convert_date(s)
    print (d)
