"""
PINWEN MU
Class: CS 521 - Spring 1
Date:3/1/2023
Final Project
Description of final project :

Pomodoro-Workout Clock 
========================  🍅 ⏰ 🍅 ⏰ 🍅  ==========================
Enter your preferred username when prompted.
Press Enter to start a 25 minutes 🍅Pomodoro clock to work.
After 25 minutes working, take a 5 minutes break. You can:
Press "l" to lie horizontally🛀.Press "s" to have a stretch🧘🏻.
After 4 Pomodoro clocks,take a 20 minutes break. You can
Press "l" to lie horizontally🛀.Press "w" to have a workout💪🏻.
Press Ctrl+C to exit.
You can check your total work and exercise time in the records.csv.
===================================================================
"""
from pomodoro import Pomodoro
import time
import csv
import random
import os.path

def work_time(pomo):
     """Start a 25 minutes Pomodoro clock."""
     while True:
        print('\nPress Enter to start a 🍅Pomodoro. ')
        if input() == '':
            pomo.countdown(pomo.work_time,'\nIt is time to take a break🛋')
            count['Pomodoro']+=25 #add 25 minutes working time to the count dictionary
            break
        else:
            print('Wrong input!')
            continue

def short_break(pomo):
    """Take a 5 minutes break. You can choose to have a strech or just lie down to rest"""
    while True:
        print('\nPress "l" to lie horizontally🛀.Press "s" to have a stretch🧘🏻.') 
        inp=input()   
        if inp == 'l':
            pomo.countdown(pomo.short_break,'\nIt is time to work⏰')
            break
        if inp == 's':
            pomo.stretching('https://www.youtube.com/watch?v=xRH1To_xyr8')
            pomo.countdown(pomo.short_break,'\nIt is time to work⏰')
            count['Exercise']+=5 #add 5 minutes exercise time to the count dictionary
            break
        else:
            print('Wrong input!')
            continue

def long_break(pomo):
    """Take a 30 minutes break. You can choose to have a workout or just lie down to rest"""
    while True:
        print('\nPress "l" to lie horizontally🛀.Press "w" to have a workout💪🏻.')
        inp=input()
        if inp == 'l':
            pomo.countdown(pomo.long_break,'\nIt is time to work⏰')
            break
        if inp == 'w':
            pomo.workout('https://www.youtube.com/watch?v=UItWltVZZmE')
            pomo.countdown(pomo.long_break,'\nIt is time to work⏰')
            count['Exercise']+=20 #add 20 minutes exercise time to the count dictionary
            break
        else:
            print('Wrong input!')
            continue

if __name__=='__main__':
    username=input('Please enter your username: ')  
    pomo=Pomodoro(username) #instantiate the Pomodoro class
    count={} #the dictionary of work and exercise time
    count['Username']=pomo.username
    count['Date']=time.strftime("%Y-%m-%d", time.localtime())
    count['Pomodoro']=0
    count['Exercise']=0

    with open('quotes.txt') as quo: #some quotes to inspire you
        file=quo.read()
    sentence=file.split('\n') #list of sentences in quotes.txt

    records_file = "records.csv"
    records_exists=os.path.isfile(records_file) #check wether the records.csv exists
    insist_days=0
    try:
        if records_exists: 
            with open(records_file, 'r') as records:
                date=[]
                data=csv.DictReader(records)
                for col in data:
                    date.append(col['Date']) #read the "Date" column in records.csv
                insist_days=len(set(date)) #maybe you have several records in one day,use set to remove duplication
    except IOError:
        print("I/O error")

    n=1
    while n>0:
        try:
            if n%4==0: #after three short breaks, take a long break
                work_time(pomo)
                long_break(pomo)
            else:
                work_time(pomo)
                short_break(pomo)
            
            n+=1            
        except KeyboardInterrupt: #Ctrl+C to exit
            print(f'\n\n{pomo.username}, good job!\n\n',random.choice(sentence),f"\n\n🎆Keep going! You have insisted {insist_days} day(s)!",'\n👋 goodbye\n')
            break
        except Exception as ex:       
            print(ex)
            exit(1)
        else:        
            if n>10: #take 135 minutes to loop one time, loop ten times in one day at most
                break

    records_columns=tuple(count.keys()) #use tuple to store dictionary keys as the csv file fieldnames
    try:
        with open(records_file, 'a') as records:
            writer = csv.DictWriter(records, fieldnames=records_columns)
            if not records_exists:
                writer.writeheader() # file doesn't exist yet, write a header
            writer.writerow(count) #write the work and exercise time into the records file
    except IOError:
        print("I/O error")






    









