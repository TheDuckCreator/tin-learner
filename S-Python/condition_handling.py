# Function for handover Hello in Another lang
def say_hello(country_name):
    # Let them be lower case
    country_lower = country_name.lower()
    if (country_lower == 'thailand'):
        print('Sawasdee')
    elif (country_lower == 'usa'):
        print('Hello')
    elif(country_lower == 'china'):
        print('Ni Hao')
    else:
        print('Hi')


country = input('input your country name')
say_hello(country)
