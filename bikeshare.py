# import depending libraries

import time
import pandas as pd
import numpy as np

# dictonary with city names and their corresponding csv data files

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

# dictonary with all the possible month and the all-month option
MONTH_DATA = {'january': '1',
              'february': '2',
              'march': '3',
              'april': '4',
              'may': '5',
              'june': '6',
              'all': '7'}

# list with the days of the week and the all-week option
DAY_DATA = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', ' saturday', 'sunday', 'all']


# get user input for filtering the data. The function askes after city, month and day for
# the data selection and hands back the city, month and day for the creation of the data frame

def get_filters():
    city = ''
    month = ''
    day = ''

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to
    # handle invalid inputs

    # while loop to ask for user input and specify one of the three citys
    while city not in CITY_DATA.keys():
        print('Please choose from which of the three following citys you want to explore the data:\n'
              '1. Chicago, 2. New York City, 3. Washington \n')
        city = input('Enter city name: ').lower()

        if city not in CITY_DATA.keys():
            print('\n Invalide Input: Please check that your input confirms to the input format.\n'
                  'The input must be one of the three city names above.')

        print('\n Your chosen city is: {}\n'.format(city.title()))

    # TO DO: get user input for month (all, january, february, ... , june)
    # while loop to ask for user input and specify one of the six month or the all month option
    while month not in MONTH_DATA.keys():
        print('Please choose the month between January and June for which you want to see the data.\n'
              'The programm accepts as input the full name of the month or the option all if you want to see the data for all month between January and June.\n')
        month = input('Enter the name of the month or "all" for the whole time period: ').lower()

        if month not in MONTH_DATA.keys():
            print('\n Invalide Input: Please check that your input confirms to the input format.\n'
                  'The input must be the full name of one of the six month between January and June or all if you want to see data for the whole time.')

        print('\n Your chosen month is: {}\n'.format(month.title()))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # while loop to ask for user user input for one of the 7 days of the week and the option whole week
    while day not in DAY_DATA:
        print(
            'Please choose a day of the week for which you want to see the data or choose all to see data for the whole week.\n'
            'The programm accepts as input the full name of the day (e.g. Monday, Tuesday,...) or the option "all" if you want to see the data for the whole week.\n')
        day = input('Enter day or option "all": ').lower()

        if day not in DAY_DATA:
            print('\nInvalide Input: Please check that your input confirms to the input format.\n'
                  'The input must be the full name of one of seven days of the week or all if you want to see data for the whole week.')

            print('\n Your chosen day is: {}\n'.format(day.title()))

    # print user input summary
    print('\n You have chosen to view data for: \n City: {} \n Month: {} \n Day: {}'.format(city.title(), month.title(),
                                                                                            day.title()))
    print('-' * 80)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    print('Data is loading...')

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time and End Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    # print success message and city, month and day for which the data was loaded
    print('Data has loaded.')
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    com_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('The most common month is:', months[com_month - 1].title())

    # TO DO: display the most common day of week
    com_day = df['day_of_week'].mode()[0]
    print('The most common day is:', com_day.title())

    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    com_start_hour = df['Start Hour'].mode()[0]
    print('The most common start hour is:', com_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip. Calculates
    the most popular start- and end-station and the most popular trips"""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    com_start_station = df['Start Station'].mode()[0]
    print('The most popular start Station is:', com_start_station.title())

    # TO DO: display most commonly used end station
    com_end_station = df['End Station'].mode()[0]
    print('The most popular end Station is:', com_end_station.title())

    # TO DO: display most frequent combination of start station and end station trip
    # generate new data column that combines Start Station and End Station for each trip
    df['Trips'] = (df['Start Station'] + ' - ' + df['End Station'])
    com_trip = df['Trips'].mode()[0]
    print('The most popular Trip is:', com_trip.title())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # create trip_duration in date_time
    df['trip_duration'] = (df['End Time'] - df['Start Time'])
    sum_travel_time = df['trip_duration'].sum()
    print('The total travel time for all trips is:', sum_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = time.strftime('%H:%M:%S', time.gmtime(df['Trip Duration'].mean()))
    print('The mean travel time is:', mean_travel_time, 'hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_typs = df['User Type'].value_counts()
    print('There are the following numbers of user per typ:\n', count_user_typs, '\n')

    # TO DO: Display counts of gender
    # since not all the data frames have a gender and birth column the try function is used
    try:
        gender_count = df['Gender'].value_counts()

        print('The count of gender is:\n', gender_count, '\n')

    except:
        print('The data for this city has no gender data.\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        min_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print('The oldest costumer was born in:', int(min_year),
              '\n The youngest costumer was born in:', int(most_recent_year),
              '\n Most of the costumers were born in:', int(common_year))
    except:
        print('The data for this city has no data about the birth dates of the costumers.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


# function to show the user raw data
def show_raw_data(df):
    print('\n Do you want to see raw data for your choosen city and time period?\n')
    answer = input('Enter yes or no: ').lower()

    start_line = 0
    while answer == 'yes':
        print(df.iloc[start_line:start_line + 10])
        start_line += 10
        answer = input('\n Would you like to see the following 10 lines of raw data also?\n'
                       'Enter yes or no: ').lower()
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
