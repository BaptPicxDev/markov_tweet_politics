import datetime as dt
from dateutil import tz


def get_datetime():
    return dt.datetime.now(tz=tz.gettz("Europe/Paris"))


def get_date():
    return get_datetime().date()
