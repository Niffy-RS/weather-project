import csv
from datetime import date, datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # Pull date from date.time module in ISO 8601 format
    relevant_date = datetime.fromisoformat(iso_string)
    # convert ISO format to Weekday Day Month Year
    format_date = relevant_date.strftime("%A %d %B %Y")
    return format_date



def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """ 
    # create value for temp_in_c variable by calculating F to C conversion
    temp_in_c = (float(temp_in_fahrenheit) - 32.00) * 5 / 9
    # round output to 1 decimal place
    return round(temp_in_c, 1)

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    total = 0
    # Create for loop to gather the values from each line in the list
    for value in weather_data:
        # calculate the sum of each value (convert str and int to float) - assign to the "total" variable
        total = total + float(value)
    # calculate total sum of values by the number of item in the list
    return total / len(weather_data)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    # create list to store csv data
    data = []
    # specify the file to open and mode for the actions (read)
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        # Skip the header
        next(reader, None)
        for row in reader:
            # Remove empty spaces and convert temperature float to int
            if row: 
                data.append([row[0], int(row[1]), int(row[2])])
    return data





def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    # Do not continue through the code if there are no lines in the list
    if len(weather_data) == 0:
        return ()
    # convert str and int to float - assign the smallest value in the weather_data list to min_value variable
    min_value = float(min(weather_data))
    # create a for loop to work backwards through the list to identify last matching min_value and its position in the list
    for position in range(len(weather_data)-1, -1, -1):
        value = weather_data[position]
        # when the min_value parameters match an item in the weather_data list, return that value and the position in the list  
        if min_value == float(value):
            return (min_value,position)


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if len(weather_data) == 0:
        return ()
    max_value = float(max(weather_data))
    for position in range(len(weather_data)-1, -1, -1):
        value = weather_data[position]
        if max_value == float(value):
            return (max_value,position)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # Create new lists 
    min_temps = []
    max_temps = []
    days = []
    # Add items from weather_data to new lists
    for value in weather_data:
        min_temp = value[1]
        min_temps.append(min_temp)
        max_temp = value[2]
        max_temps.append(max_temp)
        day = value[0]
        days.append(day)
    
    # calculating required info
    avg_low = calculate_mean(min_temps)
    avg_high = calculate_mean(max_temps)
    min_value, min_position = find_min(min_temps)
    min_day = days[min_position]
    max_value, max_position = find_max(max_temps)
    max_day = days[max_position]
    num_days = len(weather_data)

    # formatting
    format_avg_low = format_temperature(convert_f_to_c(avg_low))
    format_avg_high = format_temperature(convert_f_to_c(avg_high))
    format_min_value = format_temperature(convert_f_to_c(min_value))
    format_max_value = format_temperature(convert_f_to_c(max_value))
    format_min_day = convert_date(min_day)
    format_max_day = convert_date(max_day)

    # make it pretty and bundle up into "summary" variable
    summary = f"{num_days} Day Overview\n"
    summary += f"  The lowest temperature will be {format_min_value}, and will occur on {format_min_day}.\n"
    summary += f"  The highest temperature will be {format_max_value}, and will occur on {format_max_day}.\n"
    summary += f"  The average low this week is {format_avg_low}.\n"
    summary += f"  The average high this week is {format_avg_high}.\n"

    return summary

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # create "daily_summary" variable to add formatted values to
    daily_summary = ""
    # using the functions created - format the values in the list and assign to relevant variables
    for value in weather_data:
        day = convert_date(value[0])
        min_temp = format_temperature(convert_f_to_c(value[1]))
        max_temp = format_temperature(convert_f_to_c(value[2]))
        # format the output - add new daily_summary lines which call the formatted variables
        daily_summary += f"---- {day} ----\n"
        daily_summary += f"  Minimum Temperature: {min_temp}\n"
        daily_summary += f"  Maximum Temperature: {max_temp}\n\n"
    return daily_summary

