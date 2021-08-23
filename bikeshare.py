#!/usr/bin/env python
# coding: utf-8

# In[80]:



import time
import pandas as pd
import numpy as np
from tkinter import filedialog
from tabulate import tabulate




def get_filters():
   

    print('Welcome to US bikeshare sharing data :)')
    
    while True:
        city = input("\n Which city would you like to filter by?  New York City, Chicago or Washington?\n")
        city=city.title()
        if city not in ('New York City', 'Chicago', 'Washington'):
            print("Sorry, I didn't catch that. Try again.")
            continue
        else:
               break
    

   

    while True:
        month = input("\n Which month would you like to filter by ?January, February, March, April, May, June \n or type 'all' if you do not have any preference?\n")
        month=month.title()
            
       
        if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
            print("Sorry, I didn't catch that. Try again.")
            continue
        else:
             break

  
    while True:
        day = input("\n Are you looking for a particular day?\n  Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday  \n  or type 'all' if you do not have any preference.\n")
        day= day.title()
    

        if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'):
            print("Sorry, I didn't catch that. Try again.")
            continue
        else:
               break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
 
    CITY_DATA  = filedialog.askopenfilename(initialdir="C:/", title="select file",filetypes=(("CSV Files","*.csv"), ("all files", "*.*")))
    df = pd.read_csv(CITY_DATA)

    df['Start Time'] = pd.to_datetime(df['Start Time'])

   

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

   
    if month != 'All':
   
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

   
        df = df[df['month'] == month]

    if day != 'All':
       
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
   

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popularMonth = df['month'].mode()[0]
    pm = popularMonth


    # TO DO: display the most common day of week

    popularDay = df['day_of_week'].mode()[0]
    pd= popularDay



    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popularHour = df['hour'].mode()[0]
    ph= popularHour
    
    T1={'Most Common Month' : [pm]  , 'Most Common day':[pd] , 'Most Common Hour:' :[ph]}
    head = ["Most Common Month", "Most Common day" , "Most Common Hour"]
    print(tabulate(T1,headers=head, tablefmt='fancy_grid'))
    
   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    

print("Displays statistics on the most popular stations and trip")

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    SS = df['Start Station'].value_counts().idxmax()
    
    # TO DO: display most commonly used end station

    ES = df['End Station'].value_counts().idxmax()
    
    # TO DO: display most frequent combination of start station and end station trip

    CS = df.groupby(['Start Station', 'End Station']).count()

    T1={'Most Commonly used start station' : [SS]  
        , 'nMost Commonly used end station':[ES]
        ,'Most Commonly used combination of start and end trip' : [SS + ES] }
                                                                
    
    head = ["Most Commonly used start station", "Most Commonly used end station" ,"Most Commonly used combination \n of start and end trip"]
    print(tabulate(T1,headers=head, tablefmt='fancy_grid')) 
  
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    TotalTravelTime = sum(df['Trip Duration'])
    TTT= TotalTravelTime/86400


    # TO DO: display mean travel time

    MeanTravelTime = df['Trip Duration'].mean()
    MTT= MeanTravelTime/60

    T1={'Total travel time' :[TTT ] , 'Mean travel time':[MTT  ]  }
    head = ["Total travel time", "Mean travel time"]
    print(tabulate(T1,headers=head, tablefmt='fancy_grid'))
    
   
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    #print(user_types)
    UY= user_types
    
    T1={'User Types' :[UY]  }
    head = ["User Types"]
    print(tabulate(T1,headers=head, tablefmt='fancy_grid'))


    # TO DO: Display counts of gender

    try:
        gender_types = df['Gender'].value_counts()
        GY= gender_types
    except KeyError:
        print("\nGender Types:\nNo data available for this month.")
        
    T2={'Gender Types' :[GY]  }
    head = ["Gender Types"]
    print(tabulate(T2,headers=head, tablefmt='fancy_grid'))

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        EarliestYear = df['Birth Year'].min()
        EY= EarliestYear
    except KeyError:
        print("\nEarliest Year:\nNo data available for this month.")

    try:
        MostRecentYear = df['Birth Year'].max()
        MRY= MostRecentYear
    except KeyError:
        print("\nMost Recent Year:\nNo data available for this month.")

    try:
        MostCommonYear = df['Birth Year'].value_counts().idxmax()
        MCY= MostCommonYear
    except KeyError:
        print("\nMost Common Year:\nNo data available for this month.")
        
        
    T3={'Earliest Year':[EY], 'Most Recent Year':[MRY] , 'Most Common Year': [MCY] }
    head = [ "Earliest Year","Most Recent Year","Most Common Year"]
    print(tabulate(T3,headers=head, tablefmt='fancy_grid'))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    while True: 
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        if view_data=='no':
            break
       
        start_loc = 0
        keepGoing = True
        while(keepGoing):
            VD=df.iloc[start_loc:start_loc + 5]
            T3={'VD':[VD] }
            head = [ "view 5 rows of individual trip data"]
            print(tabulate(T3,headers=head, tablefmt='fancy_grid'))
            start_loc += 5
            view_display = input("Do you wish to continue?: ").lower()
            if view_display == "no": 
                keepGoing = False

        else: 
            break
        
   
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
       

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            


if __name__ == "__main__":
    main()





# In[ ]:




