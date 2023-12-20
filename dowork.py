# Author: Phil Aufdencamp
# Main script which you run to do work
# Dev List
# IN PROGRESS

# TODO
# (X): Show a preview of all the exercises in  a scheduled routine prior to 
#    entering the routine, with a pause to continue or not

# MVP Features:
# ( ): At the end of each exercise, show what the next exercise is so that you
#    can get ready for it
# ( ): implement a pause function

# NICE TO HAVE FEATURES
# ( ): Set up an auto advance setting
#    ( ): Set up a "settings" dictionary with keys for each settings and 
#         settable corresponding values
# ( ): Create functionality for circuit sets
# ( ): Change from phase to phase based on calendar days with auto advance
#     based on compliance with the work so far
# ( ): Automate progress across the plan based on compliance and feedback,
#      maybe with an index variable
# ( ): print post workout feedback based on the report 

# GLORIOUS FUTURE
# ( ): Refactor to use a state machine rather than a series of state machines 
#    with inputs. This will allow the user a "back button"
#    ( ): Make a list of all the features and functionality that currently work 
#         so that I can test it and verify no regressions post refactor
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

# set the path to FFmpeg executable -> this may not actually be needed, will try 
# deleting it later
pydub.AudioSegment.converter = "/usr/local/bin/ffmpeg"

# do the imports from other classes i've written
from exercise import Generic
from exercise import Interval
from exercise import Reps_Based
from exercise import Time_Based

# define a function play a tone of arbitrary frequency (Hz) and duration (sec)
def play_tone(frequency,duration):
     #Generate a sine wave of the specified frequency and duration
     sine_wave = Sine(frequency).to_audio_segment(duration=duration*1000) 

     #Play the generated sine wave
     sine_wave.export("temp.wav",format="wav")
     subprocess.run(["afplay", "temp.wav"], check=True)

# define a function to return the workout for today based on a schedule
def scheduled_workout():

     # Get the current date and time
     current_datetime = datetime.datetime.now()

     # Get the day of the week as a string
     day_of_week_string = current_datetime.strftime('%A') #Returns "Wednesday" ie
     print(day_of_week_string)

     weekly_plan = {
          'Sunday':['P3 Rehab','P1.2 Recovery Floor Work',
               'GMB Wrist P1'],
          'Monday':['P3 Rehab','P1.2 Recovery Floor Work','Trainer Work',
               'GMB Wrist P1'],
          'Tuesday':['P3 Rehab','P1.2 Recovery Floor Work',
               'P0.2 Banded, Modified','GMB Wrist P1'],
          'Wednesday':['P3 Rehab','P1.2 Recovery Floor Work','Trainer Work',
               'GMB Wrist P1'],
          'Thursday':['P3 Rehab','P1.2 Recovery Floor Work',
               'P0.2 Ramping, Modified','GMB Wrist P1'],
          'Friday':['P3 Rehab','P1.2 Recovery Floor Work','Trainer Work',
               'GMB Wrist P1'],
          'Saturday':['P3 Rehab','P1.2 Recovery Floor Work',
               'GMB Wrist P1']
               } 
     return weekly_plan.get(day_of_week_string, None)

# plays a 3-2-1 type tone to start
def ready_set_go(one_liner):
     for i in range(3):
          os.system('clear')
          print(f"get ready to do {one_liner}")
          print(3-i)
          play_tone(440, 0.5)
          time.sleep(0.125)
     play_tone(880,0.5)

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
     todays_routine = database.get(workout_name, None)
     report = [None] * len(todays_routine)
     index = 0
     for each in todays_routine:
          print(each.name)
     # eventually this user input will factor into a state machine and 
     # allows the user to go back to a previous menu, but for now 
     # it's essentially acting as a pause button
     continue_yn = input("Enter to continue with scheduled Routine")
     for each in todays_routine:
          if isinstance(each,Time_Based):
               print(f"Do a {each.name} with {each.load} for "
                     f" {each.duration} seconds.")
               time.sleep(7)
               ready_set_go(each.name)
               count_down(each.duration, each.name)
               print(each.name)
               print(f" [d] for done, [s] for skipped, [i] for incomplete")
               report[index] = input()

          elif isinstance(each,Reps_Based):
               print(f"Do a {each.name} with {each.load} pounds for "
                     f" {each.reps} reps.")
               print(f" [d] for done, [s] for skipped, [i] for incomplete")
               report[index] = input()

          elif isinstance(each,Generic):
               print(f"Do {each.name} with {each.load} according to "
                     f"{each.instructions}")
               print(f" [d] for done, [s] for skipped, [i] for incomplete")
               report[index] = input()

          elif isinstance(each,Interval):
               print(f"Get Ready for {each.name}")
               # Give the user a preview of what they are going to be doing
               interval_index = 0
               for element in each.instructions:
                    print(f"{each.instructions[interval_index]} @ "
                         f"{each.load[interval_index]} for "
                         f"{each.times[interval_index]} seconds")
                    interval_index = interval_index + 1
               time.sleep(7)
               ready_set_go(each.name)
               interval_index = 0
               for element in each.instructions:
                    workout_text = f"Do {each.instructions[interval_index]} @ " \
                    f"{each.load[interval_index]} "
                    print(workout_text)
                    count_down(each.times[interval_index],workout_text)
                    interval_index = interval_index + 1

          index = index + 1
          os.system('clear')
     return report
    
# define the routines we want to do, put them in a dictionary
routines = {
     'P1 Banded': [Time_Based("Plank","Bodyweight",45),
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
     'P1 Ramping': [Time_Based("Plank","Bodyweight",45),
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
     'P1 Hip Mobility': [Generic("Cycling Recovery","Theragun","See App"),
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
     'GMB Wrist P1': [Time_Based("Wrist Circles, CW",0,30),
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
          Time_Based("Rear Facing Wrist Hold",0,5)],
     'GMB Wrist P2': [Time_Based("Wrist Circles, CW",0,30),
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
     'P1 Shoulder Mobility': [Generic("Shoulders","Theragun","See App"),
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
     'P3 Rehab': [Time_Based("Elevated Ankle Dorsiflexion, Right",0,60),
          Time_Based("Plantar Fascia Mobilization",0,60),
          Reps_Based("Heel Raises w/ Counter Support",0,20), #Set 1
          Time_Based("Single Leg Stance, Right",0,30),
          Reps_Based("Single Leg Sit to Stand, High Surface, Right",0,10),
          Reps_Based("Banded Side Step","vLight",20),
          Reps_Based("4-Way Reach",0,5),
          Reps_Based("Heel Raises w/ Counter Support",0,20), #Set 2
          Time_Based("Single Leg Stance, Right",0,30),
          Reps_Based("Single Leg Sit to Stand, High Surface, Right",0,10),
          Reps_Based("Banded Side Step","vLight",20),
          Reps_Based("4-Way Reach",0,5),
          Reps_Based("Heel Raises w/ Counter Support",0,20), #Set 3
          Time_Based("Single Leg Stance, Right",0,30),
          Reps_Based("Single Leg Sit to Stand, High Surface, Right",0,10),
          Reps_Based("Banded Side Step","vLight",20),
          Reps_Based("4-Way Reach",0,5)],
     'P1.2 Recovery Floor Work': [Time_Based("Forward Fold",0,60),
          Time_Based("Bow Stretch, Left",0,60),
          Time_Based("Bow Stretch, Right",0,60),
          Time_Based("Lying Spine Twist, Left",0,60),
          Time_Based("Lying Spine Twist, Right",0,60)],
     'P0.2 Banded, Modified': [Time_Based("Kneeling Plank",0,45),
                  Reps_Based("Bicycle Crunch",0,10),
                  Time_Based("Banded Bridge Abduction","Light",45),
                  Time_Based("Banded Bridge","Medium Band",45),
                  Time_Based("Lying Banded Front Raise","Light Band",45),
                  Time_Based("Lying Banded Chest Press","Medium Heavy Band",45),
                  Time_Based("Banded Row, Single Foot","Medium Heavy Band",45)],
     'P0.2 Ramping, Modified': [Time_Based("Kneeling Plank",0,45),
               Reps_Based("Bicycle Crunch",0,10),
               Interval("Iso Bridge",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5]),
               Interval("Iso Banded Bridge Abduction",["Press","Press","Press"],
                           ["50%","80%","110%"],[20,10,5]),
               Interval("Iso Narrow Knees",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5]),
               Interval("Iso Neck Triceps Extension",["Press","Press","Press"],
                           ["50%","80%","110%"],[20,10,5]),
               Interval("Iso Butterfly Crunch",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5]),
               Interval("Iso Lying Front Raise",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5]),
               Interval("Iso Lying Chest Press",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5]),
               Interval("Iso Single Foot Row",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5])],
     'Interval Test': [Interval("Ramping Squat",
          ["Press ","Press ","Press "],["50%","80%","100%"],[20,10,5])],
     'Trainer Work': [Generic("Trainer Road Workout","Bike","Open the TR Apo")],
     'Timer Test': [Time_Based("Timer_Test",0,15)]
}

# Where the magic happens
# this makes it so that this code only runs when this is the main method
if __name__ == "__main__": 
     with open('workout_plan.yaml', 'w') as file:
          yaml.dump(routines, file)

     #index variable is used regardless of what the user selecs
     index = 0
     # prompt the user to do what is currently scheduled vs selecting one from the 
     # routines which are available
     
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
