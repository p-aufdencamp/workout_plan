# Author: Phil Aufdencamp
# Main script which you run to do work
# Dev List
# IN PROGRESS
############################################################################
# Feature Branch Goals / Description
# Implement a "settings" dictionary so that we can do things like test mode,
# multiple users, etc
# This branch will be considered complete when we have moved the 
# scheduled vs ala carte to the settings file, 
# Introduced multiple user profiles
# Refactored the storage of the strength/rehab/etc workouts so that they 
# return different answers for different users

# TODO
# (X): Introduce a settings dictionary, populated by a function
# (X): Collect settings of ala_carte_vs_schedule
# (X): Collect settings re: which user
# (X): Pass the settings file to the scheduled_workout function so that it 
#    can keep a Philou schedule as well as a Claudi Schedule

# Code Best Practices:
# ( ): no need for an intermediate variable between the settings dictionary
#    and the logic which requires it, eliminate this.
# ( ): Refactor the workout containing python files to use a dictionary instead of a series of if statements

# MVP Features:
# ( ): implement a skip function
# ( ): implement a pause function


# NICE TO HAVE FEATURES
# ( ): If there isn't a scheduled workout on the weekly plan, give the user a 
#    friendly message to see the ala carte menu instead of erroring out
# ( ): Set up an auto advance setting
#    ( ): Set up a "settings" dictionary with keys for each settings and 
#         settable corresponding values
# ( ): Create functionality for circuit sets
# ( ): Migrate the routine data base to a YAML
# ( ): Migrate the plan to a YAML
# ( ): Change from phase to phase based on calendar days with auto advance
#     based on compliance with the work so far
# ( ): Automate progress across the plan based on compliance and feedback,
#      maybe with an index variable
# ( ): print post workout feedback based on the report 

# GLORIOUS FUTURE
# ( ): Automated pre-commit testing
# ( ): Build a "textual" UI
# ( ): Divorce the front end UI from the "business logic"
# ( ): Add some functionality for different users and/or profiles
# ( ): Add a back button from the workout preview back to the scheduled/ala 
#    carte screen
# ( ): do some error handling in the do_work function so that if the 
#      requested routine isn't in the database, it doesn't get mad
# ( ): Set up a "test" mode so that I can test the code without affecting the 
#    tracking compliance or other reported metrics
# ( ): Do some error handling in the scheduled workout function so that if 
#       today doesn't have a scheduled workout, it doesn't get mad

# Per Commit Tests to Run
# ( ): scheduled workout runthrough
# ( ): ala carte workout runthrough, Reps_Based
# ( ): ala carte workout runthrough, Timne_Based
# ( ): ala carte workout runthrough, Generic
# ( ): ala carte workout runthrough, Interval

# import from big python libraries
import datetime
import os
import numpy
import pyaudio
import pydub
from pydub import AudioSegment
from pydub.generators import Sine
import subprocess
import time
import yaml



# do the imports from other classes and files i've written
from exercise import Generic
from exercise import Interval
from exercise import Reps_Based
from exercise import Time_Based

import cardio
import mobility_a
import rehab_mobility
import rehab_strength
import strength_a
import strength_b
import wrist_strength


# prompts the user for a series of settings, then writes the settings 
# dictionary based on the responses to those prompts
def collect_settings():

     settings = {} #initialize an empty dictionary
     os.system('clear')
     # First Setting: Which user
     print("Hello, welcome to the ClaufdenGym. What's your name?")
     print("[c] for Claudi")
     print("[p] for Philou")
     print("[g] for guest")
     settings['selected_user'] = input("Type an option" \
          " from the brackets and hit enter")
     os.system('clear')

     # Second setting: Scheduled vs ala carte mode
     print("Tell me some settings for this session")
     print("which workout would you like to do?")
     print("[s] for scheduled")
     print("[a] for ala carte")
     settings['schedule_mode'] = input("Type an option" \
          " from the brackets and hit enter")
     os.system('clear')

     return settings

# waits the duration of the time, then 
# counts down via 3-2-1 again
def count_down(timespan, one_liner):
     if(timespan>3):
          for i in range(timespan-3):
               os.system('clear')
               print(f"{timespan-i} seconds remaining for {one_liner}")
               time.sleep(1)
          
          for i in range(3):
               os.system('clear')
               print(3-i)
               play_tone(440, 0.5)
               time.sleep(0.125)
          play_tone(880,0.5)
     else:
          for i in range(3):
               os.system('clear')
               print(3-i)
               play_tone(440, 0.5)
               time.sleep(0.125)
          play_tone(880,0.5)

# define a function to actually do a routine
def do_work(database,workout_name):
     # function to perform a workout routine located in the database
     os.system('clear')
     print(workout_name)
     active_routine = database.get(workout_name, None)
     report = [None] * len(active_routine)
     index = 0
     for each in active_routine:
          print(each.name)
     # eventually this user input will factor into a state machine and 
     # allows the user to go back to a previous menu, but for now 
     # it's essentially acting as a pause button
     continue_yn = input("Enter to continue with scheduled Routine")

     for i in range(len(active_routine)):
          current = active_routine[i]
          try:
               next = active_routine[i+1]
               if isinstance(current,Time_Based):
                    print(f"Do a {current.name} with {current.load} for "
                         f" {current.duration} seconds.")
                    time.sleep(7)
                    ready_set_go(current.name)
                    count_down(current.duration, current.name)
                    print(current.name)
                    
               elif isinstance(current,Reps_Based):
                    print(f"Do a {current.name} with {current.load} pounds for "
                         f" {current.reps} reps.")

               elif isinstance(current,Generic):
                    print(f"Do {current.name} with {current.load} according to "
                         f"{current.instructions}")

               elif isinstance(current,Interval):
                    print(f"Get Ready for {current.name}")
                    # Give the user a preview of what they are going to be doing
                    interval_index = 0
                    for element in current.instructions:
                         print(f"{current.instructions[interval_index]} @ "
                              f"{current.load[interval_index]} for "
                              f"{current.times[interval_index]} seconds")
                         interval_index = interval_index + 1
                    time.sleep(7)
                    ready_set_go(current.name)
                    interval_index = 0
                    for element in current.instructions:
                         workout_text = f"Do " \
                         f"{current.instructions[interval_index]} @ " \
                         f"{current.load[interval_index]} "
                         print(workout_text)
                         count_down(current.times[interval_index],workout_text)
                         interval_index = interval_index + 1
               print(f" [d] for done, [s] for skipped, [i] for incomplete")
               report[index] = input()
               user_ready = input(f"get ready to do {next.name}")
               index = index + 1
               os.system('clear')
          except IndexError:
               if isinstance(current,Time_Based):
                    print(f"Do a {current.name} with {current.load} for "
                         f" {current.duration} seconds.")
                    time.sleep(7)
                    ready_set_go(current.name)
                    count_down(current.duration, current.name)
                    print(current.name)
                    
               elif isinstance(current,Reps_Based):
                    print(f"Do a {current.name} with {current.load} pounds for "
                         f" {current.reps} reps.")

               elif isinstance(current,Generic):
                    print(f"Do {current.name} with {current.load} according to "
                         f"{current.instructions}")

               elif isinstance(current,Interval):
                    print(f"Get Ready for {current.name}")
                    # Give the user a preview of what they are going to be doing
                    interval_index = 0
                    for element in current.instructions:
                         print(f"{current.instructions[interval_index]} @ "
                              f"{current.load[interval_index]} for "
                              f"{current.times[interval_index]} seconds")
                         interval_index = interval_index + 1
                    time.sleep(7)
                    ready_set_go(current.name)
                    interval_index = 0
                    for element in current.instructions:
                         workout_text = f"Do " \
                         f"{current.instructions[interval_index]} @ " \
                         f"{current.load[interval_index]} "
                         print(workout_text)
                         count_down(current.times[interval_index],workout_text)
                         interval_index = interval_index + 1
               print(f" [d] for done, [s] for skipped, [i] for incomplete")
               report[index] = input()
               index = index + 1
               os.system('clear')
     return report

# define a function play a tone of arbitrary frequency (Hz) and duration (sec)
def play_tone(frequency,duration):
     #Generate a sine wave of the specified frequency and duration
     sine_wave = Sine(frequency).to_audio_segment(duration=duration*1000) 

     #Play the generated sine wave
     sine_wave.export("temp.wav",format="wav")
     subprocess.run(["afplay", "temp.wav"], check=True)

# plays a 3-2-1 type tone to start
def ready_set_go(one_liner):
     for i in range(3):
          os.system('clear')
          print(f"get ready to do {one_liner}")
          print(3-i)
          play_tone(440, 0.5)
          time.sleep(0.125)
     play_tone(880,0.5)

# define a function to return the workout for today based on a schedule
def scheduled_workout(settings):

     # Get the current date and time
     current_datetime = datetime.datetime.now()

     # Get the day of the week as a string
     day_of_week_string = current_datetime.strftime('%A') #ie "Wednesday"

     if settings['selected_user'] == "p":
          weekly_plan = {
               'Saturday': ['Rehab Mobility','Rehab Strength'],
               'Sunday': ['Rehab Mobility'],
               'Monday': ['Rehab Mobility','Mobility A','Cardio'],
               'Tuesday': ['Rehab Mobility','Rehab Strength','Wrist Strength', 
                    'Strength A'],
               'Wednesday': ['Rehab Mobility','Mobility A','Cardio'],
               'Thursday': ['Rehab Mobility','Rehab Strength', 'Wrist Strength', 
                    'Strength B'],
               'Friday': ['Rehab Mobility','Mobility A','Cardio']
          }
     elif settings['selected_user'] == "c":
          weekly_plan = {
               'Saturday': ['Rehab Mobility','Rehab Strength'],
               'Sunday': ['Rehab Mobility'],
               'Monday': ['Rehab Mobility','Mobility A','Cardio'],
               'Tuesday': ['Rehab Mobility','Rehab Strength','Wrist Strength', 
                    'Strength A'],
               'Wednesday': ['Rehab Mobility','Mobility A','Cardio'],
               'Thursday': ['Rehab Mobility','Rehab Strength', 'Wrist Strength', 
                    'Strength B'],
               'Friday': ['Rehab Mobility','Mobility A','Cardio']
          }
     else:
          weekly_plan = {
               'Saturday': ['Strength A','Mobility A'],
               'Sunday': ['Strength B','Mobility A'],
               'Monday': ['Strenght A','Mobility A'],
               'Tuesday': ['Strength A','Mobility A'],
               'Wednesday': ['Strength A','Mobility A'],
               'Thursday': ['Strength A','Mobility A'],
               'Friday': ['Strength A','Mobility A']
          }

     return weekly_plan.get(day_of_week_string, None)



# Where the magic happens
# this makes it so that this code only runs when this is the main method
if __name__ == "__main__": 

     #index variable is used regardless of what the user selecs
     index = 0
     # prompt the user to do what is currently scheduled vs selecting one from 
     # the routines which are available
     
     #print("[s] for scheduled")
     #print("[a] for ala carte")
     #scheduled_vs_ala_carte = input("select an option: ")

     settings = collect_settings() # Collect the settings from the user 
     which_schedule = settings['schedule_mode']

     active_routines = {
     'Rehab Mobility': rehab_mobility.get_rehab_mobility_routine(settings),
     'Mobility A': mobility_a.get_mobility_a_routine(settings),
     'Rehab Strength': rehab_strength.get_rehab_strength_routine(settings),
     'Wrist Strength' : wrist_strength.get_wrist_strength_routine(settings),
     'Strength A' : strength_a.get_strength_a_routine(settings),
     'Strength B' : strength_b.get_strength_b_routine(settings),
     'Cardio' : cardio.get_cardio_routine(settings)
}

     if which_schedule == "s":
          todays_workouts = scheduled_workout(settings)
          todays_reports = [None] * len(todays_workouts)
          for each in todays_workouts:
               print(each)
               
          # eventually this user input will factor into a state machine and 
          # allows the user to go back to a previous menu, but for now 
          # it's essentially acting as a pause button
          continue_yn = input("Enter to continue with scheduled workout")
          for each in todays_workouts:
               todays_reports[index] = do_work(active_routines,each)
               index = index + 1

     elif which_schedule == "a":
          os.system('clear')
          #print("select a routine from the options below")
          routine_keys = [None] * len(active_routines)
          for key in active_routines.keys():
               print(f"[{index}] {key}")
               routine_keys[index] = key
               index = index + 1
          selected_routine = input("select a routine from the library")
          selected_index = int(selected_routine)
          todays_workout_name = routine_keys[selected_index]
          print(todays_workout_name)
          report = do_work(active_routines,todays_workout_name)
    
     else:
          print ("Thanks for coming to the gym")
