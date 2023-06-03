import datetime
import pytz

class DateUtility:
    @staticmethod
    def convert_dt(from_date, from_date_tz, to_date_tz):
        """
        Converts a datetime object from one timezone to another.
        :param from_date: The datetime object to convert.
        :param from_date_tz: The source timezone.
        :param to_date_tz: The target timezone.
        :return: The converted datetime object.
        """
        from_datetime = datetime.datetime.combine(from_date, datetime.datetime.min.time())
        from_timezone = pytz.timezone(from_date_tz)
        to_timezone = pytz.timezone(to_date_tz)
        converted_dt = from_timezone.localize(from_datetime).astimezone(to_timezone)
        return converted_dt

    @staticmethod
    def add_dt(from_date, number_of_days):
        """
        Adds the specified number of days to a datetime object.
        :param from_date: The datetime object.
        :param number_of_days: The number of days to add.
        :return: The updated datetime object.
        """
        updated_dt = from_date + datetime.timedelta(days=number_of_days)
        return updated_dt

    @staticmethod
    def sub_dt(from_date, number_of_days):
        """
        Subtracts the specified number of days from a datetime object.
        :param from_date: The datetime object.
        :param number_of_days: The number of days to subtract.
        :return: The updated datetime object.
        """
        updated_dt = from_date - datetime.timedelta(days=number_of_days)
        return updated_dt

    @staticmethod
    def get_days(from_date, to_date):
        """
        Calculates the number of days between two datetime objects.
        :param from_date: The start datetime object.
        :param to_date: The end datetime object.
        :return: The number of days between the two dates.
        """
        difference = to_date - from_date
        return difference.days

    @staticmethod
    def get_days_exclude_we(from_date, to_date):
        """
        Calculates the number of business days (excluding weekends) between two datetime objects.
        :param from_date: The start datetime object.
        :param to_date: The end datetime object.
        :return: The number of business days between the two dates.
        """
        business_days = 0
        current_date = from_date

        while current_date <= to_date:
            if current_date.weekday() < 5:
                business_days += 1
            current_date += datetime.timedelta(days=1)

        return business_days

    @staticmethod
    def get_days_since_epoch(from_date):
        """
        Calculates the number of days since the Epoch.
        :param from_date: The datetime object.
        :return: The number of days since the Epoch.
        """
        epoch = datetime.datetime.utcfromtimestamp(0)
        from_datetime = datetime.datetime.combine(from_date, datetime.datetime.min.time())
        difference = from_datetime - epoch
        return difference.days


    @staticmethod
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

    @staticmethod
    def get_business_days(from_date, to_date, holiday_file):
        """
        Calculates the number of business days between two datetime objects, excluding holidays.
        :param from_date: The start datetime object.
        :param to_date: The end datetime object.
        :param holiday_file: The name of the holiday file.
        :return: The number of business days between the two dates.
        """
        holidays = DateUtility.load_holidays_from_file(holiday_file)
        business_days = 0
        current_date = from_date

        while current_date <= to_date:
            if current_date.weekday() < 5 and current_date not in holidays:
                business_days += 1
            current_date += datetime.timedelta(days=1)

        return business_days

utility = DateUtility()
start_date = datetime.date(2023, 5, 1)
end_date = datetime.date(2023, 5, 15)

converted_dt = utility.convert_dt(start_date, 'UTC', 'US/Eastern')
added_dt = utility.add_dt(start_date, 7)
subtracted_dt = utility.sub_dt(start_date, 3)
days_between = utility.get_days(start_date, end_date)
days_exclude_we = utility.get_days_exclude_we(start_date, end_date)
days_since_epoch = utility.get_days_since_epoch(start_date)
business_days = utility.get_business_days(start_date, end_date, 'holidays.dat')
