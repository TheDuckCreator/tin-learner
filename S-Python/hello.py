# Import Function from Library
from datetime import datetime, timedelta

# Function to print the day


def print_list_date(added_date):
    print('Day: ' + str(added_date.day))
    print('Month: ' + str(added_date.month))
    print('Year: ' + str(added_date.year))


# This is hello message
print('Hello World!, Welcome to my starter program')

# Input
today = datetime.now()
name = input('Input Your Name ')

print('Hello ' + name.capitalize())
print('This is ' + str(today))

age = input('Input your age ')
print('You are ' + str(age) + ' year old.')

print_list_date(today)

# Birthday
birthday = input('Input your birthday (dd/mm/yyyy) ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

# Print it Normal and Functional
print('Your birthday is on ' + str(birthday_date))
print_list_date(birthday_date)
