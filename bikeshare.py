# -*- coding: utf-8 -*-
"""
Last edited on Wed May 20 22:40:00 2020

@author: User
"""
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze. Handles incorrect user input.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    prompt_1 = '\nWould you like to see data of Chicago, New York City or Washington. Please enter the name in lowercase letters. If you want to leave now type "quit":'
    active_1 = True
    city = str()

    while active_1:
        city = str(input(prompt_1))
        if city in ('chicago','new york city','washington'):
            print('Perfect, you have selected: ' + city.upper() + '. Let\'s go on.')
            break
        elif city == 'quit':
            active_1 = False



    # get user input for month (all, january, february, ... , june)
    prompt_2 = '\nFor which month would you like to see data? Please enter the name of the month in lowercase letters). Enter "all" for all months. If you want to leave now type "quit":'
    active_2 = True
    month = str()

    while active_2:
        month = str(input(prompt_2))
        if month in ('january','february','march','april','may','june','july','august','september','october','november','december','all'):
            print('Perfect, you have selected: ' + month.upper() + '. Let\'s go on.')
            break
        elif month == 'quit':
            active_2 = False



    # get user input for day of week (all, monday, tuesday, ... sunday)
    prompt_3 = '\nFor which day would you like to see data? Please enter the day in lowercase letters. Enter "all" for all months. If you want to leave now type "quit":'
    active_3 = True
    day = str()

    while active_3:
        day = str(input(prompt_3))
        if (day == ('monday') or day == ('tuesday') or day == ('wednesday') or day == ('thursday') or day == ('friday') or day == ('saturday') or day == ('sunday') or day == ('all')):
            print('Perfect, you have selected: ' + day.upper() + '. Let\'s go on.')
            break
        elif day == 'quit':
            active_3 = False



    print('-'*40)
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

    df = pd.read_csv(CITY_DATA[city])
    df.dropna(axis = 0)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek


    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september', 'october', 'november','december']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
        day = days.index(day)
        df = df[df['day_of_week'] == day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month (January = 1,[...],December = 12):', popular_month)

    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    popular_day = df['day_of_week'].mode()[0]
    #popular_day = df.groupby(['day_of_week']).size().idxmax()
    print('Most Popular Day of week (Monday = 0,[...],Sunday = 6):', popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour= df['hour'].mode()[0]
    print('Most Popular hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)


    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    popular_comb_station = df.groupby(['Start Station','End Station']).size().idxmax()
    print('Most popular combination of stations:', popular_comb_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', int(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    try:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        count_user_types = df.pivot_table(index=['User Type'], aggfunc='size')
        print('Counts of:', count_user_types)

        # Display counts of gender

        count_genders = df.pivot_table(index=['Gender'], aggfunc='size')
        print('Counts of:', count_genders)

        # Display earliest, most recent, and most common year of birth

        early_birth_year = df['Birth Year'].min()
        print('Eearliest year of birth:', int(early_birth_year))

        late_birth_year = df['Birth Year'].max()
        print('Most recent year of birth:', int(late_birth_year))

        common_birth_year = df['Birth Year'].mode()[0]
        print('Most common year of birth:', int(common_birth_year))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

    except Exception: print("Sorry, we encountered an error generating more statistics. More statistics are not available for this selection. Please pick another city.")

def raw_data(df):
    """Displays raw data on demand, five rows at a time. Handles incorrect user input."""

    prompt_4 = '\nWould you like to see raw data for your selection. Please type "yes" or "no":'
    prompt_5 = '\nWould you like to see more raw data for your selection. Please type "yes" or "no":'
    prompt_6 = '\nPlease type "yes" or "no":'
    i = 5
    active_4 = True
    raw_data = str(input(prompt_4))

    while active_4:
        if raw_data == 'yes':
            print('Ok. printing data:\n ')
            print(df.iloc[i-5:i])
            i +=5
            raw_data = str(input(prompt_5))
        elif raw_data == 'no':
            active_4 = False
        else: raw_data = str(input(prompt_6))


def main():
    """Calls functions and handles exceptions. Asks user if a restart is wanted."""
    while True:
        try:
            city, month, day = get_filters()
            df = load_data(city, month, day)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            raw_data(df)

        except (ValueError, TypeError):
            print("Bye bye.")

        except IndexError:
            print("Sorry this data is not available. Please pick a month before July.")

        restart = input('\nWould you like to restart? Enter "yes" or "no":\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
