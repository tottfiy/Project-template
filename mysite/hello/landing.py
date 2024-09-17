import datetime


def date_checker():
    day = datetime.date.today().strftime("%d-%m")
    if day == "25-12":
        return True
    else:
        return False


