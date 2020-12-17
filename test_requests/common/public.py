import json
from datetime import datetime


def is_json(data):
    try:
        json.loads(data)
    except ValueError:
        return False
    return True


def isset(v):
    try:
        v
    except:
        return False
    else:
        return True


def if_weekend(day_str, separator = ""):
    """
    if a day is weekend
    :param day_str: string of a day
    :param separator: separator of year, month and day, default is empty
    :return: True: is weekend; False: not weekend
    """
    spec = "%Y" + separator + "%m" + separator + "%d"
    day = datetime.strptime(day_str, spec).date()
    # Monday == 0 ... Sunday == 6
    if day.weekday() in [5, 6]:
        return True
    else:
        return False
