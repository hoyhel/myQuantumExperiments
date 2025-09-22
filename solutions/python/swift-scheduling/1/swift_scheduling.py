from datetime import datetime, timedelta
import calendar
import re

def delivery_date(start, description):
    """A function to return the actual delivery date based on the given description and start datetime."""
    datetime_obj = datetime.fromisoformat(start)
    # For month, we're supposed to use the month given in the description
    month = ""
    for char in description:
        if char.isdigit():
            month += str(char)
    if month:
        month = int(month)
    year = datetime_obj.year
    start_month = datetime_obj.month
    quarters = {
        1: [1, 2, 3],  # January, February, March
        2: [4, 5, 6],  # April, May, June
        3: [7, 8, 9],  # July, August, September
        4: [10, 11, 12],  # October, November, December
    }
    quarter = ""
    for char in description:
        if char.isdigit():
            quarter += str(char)
    if quarter:
        quarter = int(quarter)

    def get_weekdays_in_month(the_year, the_month):
        """
            Returns a list of all weekdays (Monday-Friday) for a given month and year,
            formatted as ISO 8601 strings.
            """
        weekday_dates = []
        # calendar.monthrange returns the weekday of the first day and number of days in month.
        _, num_days = calendar.monthrange(the_year, the_month)

        # Loop through each day of the month
        for day in range(1, num_days + 1):
            # Create a datetime object for the current day
            current_date = datetime(the_year, the_month, day)

            # Check if the day is a weekday (Monday=0 to Friday=4)
            if current_date.weekday() < 5:
                # Append the date in ISO 8601 format to our list
                weekday_dates.append(current_date.isoformat())

        return weekday_dates

    if description == "NOW":
        datetime_obj = datetime_obj + timedelta(hours=2)
    elif description == "ASAP":
        if datetime_obj.hour < 13:
            datetime_obj = datetime_obj.replace(hour=17, minute=0, second=0)
        elif datetime_obj.hour >= 13:
            datetime_obj = datetime_obj + timedelta(days=1)
            datetime_obj = datetime_obj.replace(hour=13, minute= 0, second=0)
    elif description == "EOW":
        if datetime_obj.weekday() < 3:
            days_to_add_map = {
                0: 4, # Monday
                1: 3, # Tuesday
                2: 2, # Wednesday
            }
            days_to_add = days_to_add_map[datetime_obj.weekday()]
            datetime_obj = datetime_obj + timedelta(days=days_to_add)
            datetime_obj = datetime_obj.replace(hour=17, minute=0, second=0)
        elif datetime_obj.weekday() < 5:
            days_to_add_map = {
                3: 3, # Thursday
                4: 2, # Friday
            }
            days_to_add = days_to_add_map[datetime_obj.weekday()]
            datetime_obj = datetime_obj + timedelta(days=days_to_add)
            datetime_obj = datetime_obj.replace(hour=20, minute=0, second=0)
    elif re.fullmatch(r".*M", description):
        if start_month < month:
            weekdays = get_weekdays_in_month(year, month)
            first = weekdays[0]
            datetime_obj = datetime.fromisoformat(first)
            datetime_obj = datetime_obj.replace(hour=8, minute=0, second=0)
        else:
            weekdays = get_weekdays_in_month(year+1, month)
            first = weekdays[0]
            datetime_obj = datetime.fromisoformat(first)
            datetime_obj = datetime_obj.replace(hour=8, minute=0, second=0)
    elif re.fullmatch(r"Q.*", description):
        given_quarter = quarters[quarter]
        if any(start_month <= num for num in given_quarter):
            last_month = given_quarter[-1]
            last_month_weekdays = get_weekdays_in_month(year, last_month)
            last_weekday = last_month_weekdays[-1]
            datetime_obj = datetime.fromisoformat(last_weekday)
            datetime_obj = datetime_obj.replace(hour=8, minute=0, second=0)
        else:
            last_month = given_quarter[-1]
            last_month_weekdays = get_weekdays_in_month(year+1, last_month)
            last_weekday = last_month_weekdays[-1]
            datetime_obj = datetime.fromisoformat(last_weekday)
            datetime_obj = datetime_obj.replace(hour=8, minute=0, second=0)
    return datetime_obj.isoformat()
