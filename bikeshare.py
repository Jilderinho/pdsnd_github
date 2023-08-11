# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:42:41 2023

@author: DEBO043
"""

import time
import pandas as pd
import numpy as np
import calendar as ca

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
       
    while city not in ["chicago","washington","new york city"]:
        
        city = input("Would you like to see data for Chicago, New York City, or Washington?:").lower()
        
        if city not in ["chicago","washington","new york city"]:
            print("Make sure the city is Chicago, Washington or New York City.")
        
        
    filter_time = ""
    
    while filter_time not in ['month','day','both','none']:
        
        filter_time = input("Would you like to filter the data by month, day, both, or not at all? Type 'none' for no time filter.:").lower()
        
        if  filter_time not in ['month','day','both','none']:
            print("I did not understand. Please try again.")
        
    
    if filter_time == "both":
        
        # TO DO: get user input for month (all, january, february, ... , june)
        month = ""
        
        while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            
            month = input("Which month?:").lower()
            
            if  month not in ['january', 'february', 'march', 'april', 'may', 'june']:
                print("Make sure to enter an appropriate month or enter 'all' for all months. Only months from the first half year are accepted, i.e. january till june.")
            
            
        
    
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = ""
        
        while day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday', 'all']:
            
            day = input('Which day?:').lower()
            
            if  day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
                print("Make sure to enter an appropriate day or enter 'all' for all days. Did you perhaps make a typo?")
        
    elif filter_time == "month":
        # TO DO: get user input for month (all, january, february, ... , june)
        day = "all"
        month = ""
        
        while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            
            month = input("Which month?:").lower()
            
            if  month not in ['january', 'february', 'march', 'april', 'may', 'june']:
                print("Make sure to enter an appropriate month or enter 'all' for all months. Only months from the first half year are accepted, i.e. january till june.")
    
    
    elif filter_time == "day":
        month = "all"
        day = ""
        
        while day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday', 'all']:
            
            day = input('Which day?:').lower()
            
            if  day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
                print("Make sure to enter an appropriate day or enter 'all' for all days. Did you perhaps make a typo?")
    
    else:
        month = "all"
        day = "all"
    
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
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df =  pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        #month = months[month]
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df["month"]==month]
        #df = df.filter(month = month, axis = 0)
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day = days.index(day)
        df = df[df["day_of_week"]==day]
        #df = df.filter(day_of_week = day, axis = 0)
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    occurrences_month = df['month'].value_counts().max()
    print("Most popular month:", ca.month_name[popular_month],", with", occurrences_month, "occurrences.")

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    occurrences_day_of_week = df['day_of_week'].value_counts().max()
    print("Most popular day of week:", ca.day_name[popular_day_of_week],", with", occurrences_day_of_week, "occurrences.")

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    occurrences_hour  = df['hour'].value_counts().max()
    print("Most popular hour:", popular_hour,", with", occurrences_hour, "occurrences.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_station = df['Start Station'].mode()[0]
    occurrences_station = df['Start Station'].value_counts().max()
    print("Most common start station:", popular_station,", with", occurrences_station, "occurrences.")

    # TO DO: display most commonly used end station
    popular_station = df['End Station'].mode()[0]
    occurrences_station = df['End Station'].value_counts().max()
    print("Most common end station:", popular_station,", with", occurrences_station, "occurrences.")

    # TO DO: display most frequent combination of start station and end station trip
    print("The combination where", df.groupby(['Start Station','End Station']).size().idxmax()[0], "is the start station and", df.groupby(['Start Station','End Station']).size().idxmax()[1], "the end station is most commonly used.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum() 
    print("The total travel time is", total_travel_time / 60, "minutes.")
    
    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean() 
    print("The average travel time is", avg_travel_time / 60, "minutes.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types   
    print("The user types distribution looks like follows:\n",df['User Type'].value_counts())
    
    # TO DO: Display counts of gender
    try:
        print("The gender distribution looks like follows:\n",df['Gender'].value_counts())
    except:
        print("Gender statistics are not available for this city.")
        

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        youngest_birth_year = df['Birth Year'].min()
        oldest_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print("Youngest customer is from birth year", youngest_birth_year,".\n")
        print("Oldest customer is from birth year", oldest_birth_year,".\n")
        print("Most common birth year is", most_common_birth_year,".\n")
    except:
        print("Birth date statistics are not available for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    
    while view_data == 'yes':
        print(df.iloc[start_loc:(start_loc+5)])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()




'''
user_input = get_filters()
print(user_input)

df = load_data(user_input[0], user_input[1], user_input[2])
'''

