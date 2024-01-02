# Author: Phil Aufdencamp
# Main script which you run to do work
# Dev List
# IN PROGRESS

# Problem Statement:
# When i recieve a new workout routine from Katy, I need to update it in N places
#    1. Add it to the routine data base, at times changing around the contents 
#    of each routine because there are exercises I do 7x a week and others I do
#    3x a week.
#    2. the weekly schedule. Really I could stop doing this by not including the 
#    phase name in the weekly schedule. Yea I think i'll do that. 


# Feature branch description
# Function of this branch is to figure out how to leave the weekly schedule 
# alone, and then change what it's pointing to. The weekly schedule right now 
# is basically:
#    Saturday: 
#         1. Mobility: Ankle Rehab 
#         2. Strength: Rehab Strength
#         3. Cardio: None
#    Sunday:
#         1. Rehab Mobility
#    Monday:
#         1. Rehab Mobility
#         2. 
#    Monday: Mobility + TR
#    Tuesday: Mobility + Strength A
#    Wednesday: Mobility + TR... etc etc
# then we have another function or lookup table or something which determines
# what the appropriate "Strength A" (for example) is based on calendar days 


# Design Doc
# Gonna make it so that the weekly schedule doesn't have to change by deleting 
# references to phases in the weekly schedule. I'll at some point include phase 
# to phase changes in some other functionality somewhere. 

# TODO
# Remove Phase elements from the weekly schedule
# (X): Define the following routines
#    (X): Rehab Mobility
#    (X): Mobility A
#    (X): Rehab Strength
#    (X): Wrist Strength
#    (X): Banded Iso Strength
#    (X): Ramping Iso Strength
# ( ): Good news we can store each category of workout such as Rehab Mobility,
#    Mobility A, etc. This way we can use the commit history on the invidual 
#    files as a record of the workout progress and change over time

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



# do the imports from other classes i've written
from exercise import Generic
from exercise import Interval
from exercise import Reps_Based
from exercise import Time_Based

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
def scheduled_workout():

     # Get the current date and time
     current_datetime = datetime.datetime.now()

     # Get the day of the week as a string
     day_of_week_string = current_datetime.strftime('%A') #ie "Wednesday"

     weekly_plan = {
          'Saturday': ['Rehab Mobility','Rehab Leg Strength'],
          'Sunday': ['Rehab Mobility'],
          'Monday': ['Rehab Mobility','Mobility A','TR Trainer Work'],
          'Tuesday': ['Rehab Mobility','Rehab Leg Strength','Wrist Strength', 
               'Banded Iso Strength'],
          'Wednesday': ['Rehab Mobility','Mobility A','TR Trainer Work'],
          'Thursday': ['Rehab Mobility','Rehab Leg Strength', 'Wrist Strength', 
               'Ramping Iso Strength'],
          'Friday': ['Rehab Mobility','Mobility A','TR Trainer Work']
     }

     old_weekly_plan = {
          'Sunday':['Katy Daily Rehab P1'],
          'Monday':['Katy Daily Rehab P1','Katy Mobility Floor Work P2',
               'TR Trainer Work'],
          'Tuesday':['Katy Daily Rehab P1','Katy Strength Work P2',
               'Katy Wrist Rehab P1','MTBS Banded P0.3'],
          'Wednesday':['Katy Daily Rehab P1', 'Katy Mobility Floor Work P2',
               'TR Trainer Work'],
          'Thursday':['Katy Daily Rehab P1', 'Katy Strength Work P2',
               'Katy Wrist Rehab P1','MTBS Ramping Modified P0.3'],
          'Friday':['Katy Daily Rehab P1', 'Katy Mobility Floor Work P2',
               'TR Trainer Work'],
          'Saturday':['Katy Daily Rehab P1', 'Katy Strength Work P2']
               } 
     return weekly_plan.get(day_of_week_string, None)
    
# define the routines we want to do, put them in a dictionary
# Routines are named according to the following convention
routines = {
     'GMB Wrist': 
          [Time_Based("Wrist Circles, CW",0,30),
          Time_Based("Wrist Circles, CCW",0,30),
          Time_Based("Backwards Wrist Stretch",0,20),
          Time_Based("Backwards Wrist Stretch",0,20),
          Time_Based("Forward Wrist Stretch",0,20),
          Time_Based("Forward Wrist Stretch",0,20),
          Time_Based("Heel Palm Up, Side to Side",0,15),
          Time_Based("Wrist Shakes",0,25),
          Time_Based("Wrist Pulses",0,20),
          Reps_Based("Back of Wrist Extension",0,10),
          Reps_Based("Back of Wrist Extension",0,10),
          Reps_Based("Seal Walk",0,10),
          Reps_Based("Seal Walk",0,10),
          Time_Based("Rear Facing Wrist Hold",0,5)],
     'Rehab Mobility':
          [Time_Based("Elevated Ankle Dorsiflexion, Right",0,60),
          Time_Based("Plantar Fascia Mobilization",0,60),
          Reps_Based("Heel Raises w/ Counter Support",0,30), 
          Time_Based("Rest",0,30), #Set 1
          Reps_Based("Heel Raises w/ Counter Support",0,30), 
          Time_Based("Rest",0,30), #Set 2
          Reps_Based("Heel Raises w/ Counter Support",0,30)
          ],
     'Mobility A': 
          [Time_Based("Forward Fold",0,60),
          Time_Based("Bow Stretch, Left",0,60),
          Time_Based("Bow Stretch, Right",0,60),
          Time_Based("Lying Spine Twist, Left",0,60),
          Time_Based("Lying Spine Twist, Right",0,60),
          Reps_Based("MacKenzie Extensions",0,10)],
     'Rehab Strength': 
          [Reps_Based("Banded Side Step","vLight",20), #Set 1
          Reps_Based("Forward T",0,8),
          Reps_Based("Step up",0,12),
          Reps_Based("Reverse Lunge Squat",0,10),
          Reps_Based("Banded Side Step","vLight",20),#Set 2
          Reps_Based("Forward T",0,8),
          Reps_Based("Step up",0,12),
          Reps_Based("Reverse Lunge Squat",0,10),
          Reps_Based("Banded Side Step","vLight",20), #Set 3
          Reps_Based("Forward T",0,8),
          Reps_Based("Step up",0,12),
          Reps_Based("Reverse Lunge Squat",0,10)],          
     'Wrist Strength': 
          [Reps_Based("Wrist Extensions, Left", 6,10),
          Reps_Based("Wrist Extensions, Right", 6,10),
          Reps_Based("Wrist Extensions, Left", 6,10),
          Reps_Based("Wrist Extensions, Right", 6,10),
          Reps_Based("Wrist Extensions, Left", 6,10),
          Reps_Based("Wrist Extensions, Right", 6,10),
          Reps_Based("Hammer Twist, Left",6,10),
          Reps_Based("Hammer Twist, Right",6,10),
          Reps_Based("Hammer Twists, Left",6,10),
          Reps_Based("Hammer Twist, Right",6,10),
          Reps_Based("Hammer Twists, Left",6,10),
          Reps_Based("Hammer Twist, Right",6,10)],
     'Banded Iso Strength': 
          [Time_Based("Plank on Elbows",0,45),
          Reps_Based("Lying Side Leg Raise, Left","Bodyweight",10),
          Reps_Based("Lying Side Leg Leg, Right","Bodyweight",10),
          Time_Based("Banded Bridge","Medium Band",45),
          Time_Based("Banded Narrow Knees","Light Band",45),
          Time_Based("Banded Back Neck Hold","Light Band",45),
          Time_Based("Banded Front Neck Hold","Light Band",45),
          Time_Based("Banded Front Raise","Light Band",45),
          Time_Based("Banded Chest Press","Medium Heavy Band",45),
          Time_Based("Banded Row","Medium Heavy Band",45),
          Time_Based("Left Plank","Body Weight",45),
          Time_Based("Right Plank","Body Weight",45)],
     'MTBS Banded P1': [Time_Based("Plank","Bodyweight",45),
          Reps_Based("Lying Side Leg Raise, Left","Bodyweight",10),
          Reps_Based("Lying Side Leg Leg, Right","Bodyweight",10),
          Time_Based("Banded Bridge","Medium Band",45),
          Time_Based("Banded Narrow Knees","Light Band",45),
          Time_Based("Banded Back Neck","Light Band",45),
          Time_Based("Banded Back Neck Hold","Light Band",45),
          Time_Based("Banded Front Raise","Light Band",45),
          Time_Based("Banded Deadlift","Medium Heavy Band",45),
          Time_Based("Banded Chest Press","Medium Heavy Band",45),
          Time_Based("Banded Squat","Body Weight",45),
          Time_Based("Banded Row","Medium Heavy Band",45),
          Time_Based("Left Plank","Body Weight",45),
          Time_Based("Right Plank","Body Weight",45)],
     'MTBS Hip Mobility': [Generic("Cycling Recovery","Theragun","See App"),
                    Generic("Glutes","Theragun","See App"),
                    Reps_Based("Frog Stretch","Body Weight",8),
          Reps_Based("Kneeling Lunge Stretch, Left","Body Weight",10),
          Reps_Based("Kneeling Lunge Stretch, Right","Body Weight",10),
                    Reps_Based("Childs Pose to Up Dog","Body Weight",5),
                    Reps_Based("Hamstring Stretch, Center->Cross->Out, Left",
                               "Body Weight",10),
                    Reps_Based("Hamstring Stretch, Center->Cross->Out, Right",
                               "Body Weight",10),
                    Reps_Based("Bow Stretch, Left","Body Weight",5),
                    Reps_Based("Bow Stretch, Right","Body Weight",5),
          Reps_Based("Seated Windshield Wiper, Left","Body Weight",5),
          Reps_Based("Seated Windshield Wiper, Right","Body Weight",5),
                    Reps_Based("Active Leg Lower, Left","Body Weight",5),
                    Reps_Based("Active Leg Lower, Right","Body Weight",5),
                    Reps_Based("Toe Touch, Raised Heels","Body Weight",10),
                    Reps_Based("Toe Touch, Raised Toes","Body Weight",10)],
     'Ramping Iso Strength': [Time_Based("Plank on Elbows",0,45),
          Reps_Based("Lying Side Leg Raise, Left","Bodyweight",10),
          Reps_Based("Lying Side Leg Leg, Right","Bodyweight",10),
          Interval("Iso Bridge",["Press", "Press", "Press"],
                         ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Narrow Knees",["Press", "Press", "Press"],
                         ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Neck Triceps Extension",["Press","Press","Press"],
                         ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Butterfly Crunch",["Press", "Press", "Press"],
                         ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Front Raise",["Press", "Press", "Press"],
                         ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Chest Press",["Press", "Press", "Press"],
                         ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Row",["Press", "Press", "Press"],
                         ["50%","80%","110%"],[20,10,5]),
          Time_Based("Left Plank","Body Weight",45),
          Time_Based("Right Plank","Body Weight",45)],
     'MTBS Ramping P1': [Time_Based("Plank","Bodyweight",45),
          Reps_Based("Lying Side Leg Raise, Left","Bodyweight",10),
          Reps_Based("Lying Side Leg Leg, Right","Bodyweight",10),
          Interval("Iso Bridge",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Narrow Knees",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Neck Triceps Extension",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Butterfly Crunch",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Front Raise",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Deadlift",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Chest Press",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Squat",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Row",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5]),
          Time_Based("Left Plank","Body Weight",45),
          Time_Based("Right Plank","Body Weight",45)], 
     'MTBS Shoulder Mobility': [Generic("Shoulders","Theragun","See App"),
          Generic("Triceps","Theragun","See App"),
                                    Reps_Based("Hold the Wall, Left","BW",5),
                                    Reps_Based("Hold the Wall, Right","BW",5),
          Reps_Based("Overhead Shoulder, Left","BW",5),
          Reps_Based("Overhead Shoulder, Right","BW",5),
                                    Reps_Based("Lats Stretch, Left","BW",5),
                                    Reps_Based("Last Stretch, Right","BW",5),
                                    Reps_Based("Rib Pull, Left","BW",5),
                                    Reps_Based("Rib Pull, Right","BW",5),
          Reps_Based("Half Kneeling T Spine Twist","BW",5),
          Reps_Based("Half Kneeling T Spine Twist, Right","BW",5)],     
     'TR Trainer Work': [Generic("Trainer Road Workout","Bike",
          "Open the TR App")]
}

# Where the magic happens
# this makes it so that this code only runs when this is the main method
if __name__ == "__main__": 
     with open('workout_plan.yaml', 'w') as file:
          yaml.dump(routines, file)

     #index variable is used regardless of what the user selecs
     index = 0
     # prompt the user to do what is currently scheduled vs selecting one from 
     # the routines which are available
     
     print("[s] for scheduled")
     print("[a] for ala carte")
     scheduled_vs_ala_carte = input("select an option: ")

     if scheduled_vs_ala_carte == "s":
          todays_workouts = scheduled_workout()
          todays_reports = [None] * len(todays_workouts)
          for each in todays_workouts:
               print(each)
               
          # eventually this user input will factor into a state machine and 
          # allows the user to go back to a previous menu, but for now 
          # it's essentially acting as a pause button
          continue_yn = input("Enter to continue with scheduled workout")
          for each in todays_workouts:
               todays_reports[index] = do_work(routines,each)
               index = index + 1

     elif scheduled_vs_ala_carte == "a":
          os.system('clear')
          #print("select a routine from the options below")
          routine_keys = [None] * len(routines)
          for key in routines.keys():
               print(f"[{index}] {key}")
               routine_keys[index] = key
               index = index + 1
          selected_routine = input("select a routine from the library")
          selected_index = int(selected_routine)
          todays_workout_name = routine_keys[selected_index]
          print(todays_workout_name)
          report = do_work(routines,todays_workout_name)
    
     else:
          print ("come on, ya gotta do something today")
