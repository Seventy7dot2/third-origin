import datetime
import pytz

def convert_timezone(dt, from_tz, to_tz):
    """
    Converts a datetime object from one timezone to another.
    :param dt: The datetime object to convert.
    :param from_tz: The source timezone.
    :param to_tz: The target timezone.
    :return: The converted datetime object.
    """
    # Ensure the datetime object is naive
    if dt.tzinfo is not None:
        dt = dt.replace(tzinfo=None)

    from_timezone = pytz.timezone(from_tz)
    to_timezone = pytz.timezone(to_tz)
    converted_dt = from_timezone.localize(dt).astimezone(to_timezone)
    return converted_dt
def add_days(dt, days):
    """
    Adds the specified number of days to a datetime object.
    :param dt: The datetime object.
    :param days: The number of days to add.
    :return: The updated datetime object.
    """
    updated_dt = dt + datetime.timedelta(days=days)
    return updated_dt

def subtract_days(dt, days):
    """
    Subtracts the specified number of days from a datetime object.
    :param dt: The datetime object.
    :param days: The number of days to subtract.
    :return: The updated datetime object.
    """
    updated_dt = dt - datetime.timedelta(days=days)
    return updated_dt
def get_days_difference(start_dt, end_dt):
    """
    Calculates the number of days between two datetime objects.
    :param start_dt: The start datetime object.
    :param end_dt: The end datetime object.
    :return: The number of days between the two dates.
    """
    difference = end_dt - start_dt
    return difference.days
def get_business_days_difference(start_dt, end_dt):
    """
    Calculates the number of business days (excluding weekends) between two datetime objects.
    :param start_dt: The start datetime object.
    :param end_dt: The end datetime object.
    :return: The number of business days between the two dates.
    """
    business_days = 0
    current_dt = start_dt

    while current_dt <= end_dt:
        if current_dt.weekday() < 5:  # Monday to Friday (0 to 4)
            business_days += 1
        current_dt += datetime.timedelta(days=1)

    return business_days
def get_days_since_epoch():
    """
    Calculates the number of days since the Epoch.
    :return: The number of days since the Epoch.
    """
    epoch = datetime.datetime.utcfromtimestamp(0)
    current_time = datetime.datetime.utcnow()
    difference = current_time - epoch
    return difference.days
def get_business_days(start_date, end_date, holidays):
    """
    Calculates the number of business days between two dates, excluding holidays.
    :param start_date: The start date.
    :param end_date: The end date.
    :param holidays: A list of holiday dates.
    :return: The number of business days between the two dates.
    """
    business_days = 0
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() < 5 and current_date not in holidays:
            business_days += 1
        current_date += datetime.timedelta(days=1)

    return business_days
def load_holidays_from_file(filename):
    """
    Loads the holiday calendar from a file.
    :param filename: The name of the file.
    :return: A list of holiday dates.
    """
    holidays = []
    with open(filename, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            timezone, date_str, holiday = line.strip().split(',')
            year, month, day = map(int, date_str.split('-'))
            holiday_date = datetime.date(year, month, day)
            holidays.append(holiday_date)
    return holidays

