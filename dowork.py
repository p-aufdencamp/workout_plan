# Author: Phil Aufdencamp
# Main script which you run to do work
# Feature List
# IN PROGRESS

# TODO
# (X): update the routines to include the latest workouts from Katy
# ( ): Push the workouts forward in time
# ( ): refactor the time_based exercise type to utilize a list of times to 
#    prepare for interval training later
# ( ): implement a pause function
# ( ): Change from phase to phase based on calendar days


# BACKLOG
# ( ): print post workout feedback based on the report 
# ( ): do some error handling in the do_work function so that if the 
#      requested routine isn't in the database, it doesn't get mad
# ( ): Set up a "test" mode so that I can test the code without affecting the 
#    tracking compliance or other reported metrics
# ( ): Automate progress across the plan based on compliance and feedback,
#      maybe with an index variable
# ( ): Build a trailing average compliance metric
# ( ): Do some error handling in the scheduled workout function so that if 
#       today doesn't have a scheduled workout, it doesn't get mad
# ( ): Add a "rest" exercise type to wait between sets

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

# set the path to FFmpeg executable -> this may not actually be needed, will try deleting it later
pydub.AudioSegment.converter = "/usr/local/bin/ffmpeg"

# do the imports from other classes i've written
from exercise import Time_Based
from exercise import Reps_Based
from exercise import Generic

# define a function play a tone of arbitrary frequency (Hz) and duration (sec)
def play_tone(frequency,duration):
     #Generate a sine wave of the specified frequency and duration
     sine_wave = Sine(frequency).to_audio_segment(duration=duration*1000) 

     #Play the generated sine wave
     sine_wave.export("temp.wav",format="wav")
     subprocess.run(["afplay", "temp.wav"], check=True)

# define a function to return the workout for today based on a schedule, hard coded for now
def scheduled_workout(date):

    #starting with just hard coded plan and will go from there.
    plan = {
          datetime.date(2023,12,8):['P3 Rehab',
               'P1.2 Recovery Floor Work','P0.2 Banded, Modified'], #Fri
          datetime.date(2023,12,9):['P3 Rehab',
               'P1.2 Recovery Floor Work'], # Sat
          datetime.date(2023,12,10):['P3 Rehab',
               'P1.2 Recovery Floor Work'], # Sun
          datetime.date(2023,12,11):['P3 Rehab',
               'P1.2 Recovery Floor Work','P0.2 Banded, Modified'], #Mon
          datetime.date(2023,12,12):['P3 Rehab',
               'P1.2 Recovery Floor Work'], #Tue
          datetime.date(2023,12,13):['P3 Rehab',
               'P1.2 Recovery Floor Work','P0.2 Ramping, Modified'], #Wed
          datetime.date(2023,12,14):['P3 Rehab',
               'P1.2 Recovery Floor Work'], #Thu
          datetime.date(2023,12,15):['P3 Rehab',
               'P1.2 Recovery Floor Work','P0.2 Banded, Modified'], #Fri
          
        }
    return plan.get(date, None)

# plays a 3-2-1 type tone
def count_down():
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
          if isinstance(each,Time_Based):
               print(f"Do a {each.name} with {each.load} for {each.duration} seconds.")
               time.sleep(7)
               count_down()
               for i in range(each.duration-3):
                    os.system('clear')
                    print(each.duration-i)
                    time.sleep(1)
               count_down()
               print(each.name)
               print(f" [d] for done, [s] for skipped, [i] for incomplete")
               report[index] = input()

          elif isinstance(each,Reps_Based):
               print(f"Do a {each.name} with {each.load} pounds for {each.reps} reps.")
               print(f" [d] for done, [s] for skipped, [i] for incomplete")
               report[index] = input()

          elif isinstance(each,Generic):
               print(f"Do {each.name} with {each.load} according to {each.instructions}")
               print(f" [d] for done, [s] for skipped, [i] for incomplete")
               report[index] = input()
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
          Generic("Iso Bridge","BJJ", "20s @50%, 10s @80%, 5s @100%"),
          Generic("Iso Narrow Knees","Hold", "20s @50%, 10s @80%, 5s @100%"),
          Generic("Iso Neck Triceps Extension","BJJ",
               "20s @50%, 10s @80%, 5s @100%"),
          Generic("Iso Butterfly Crunch","Hold", "20s @50%, 10s @80%, 5s @100%"),
          Generic("Iso Front Raise","BJJ", "20s @50%, 10s @80%, 5s @100%"),
          Generic("Iso Deadlift","BJJ", "20s @50%, 10s @80%, 5s @100%"),
          Generic("Iso Chest Press","BJJ", "20s @50%, 10s @80%, 5s @100%"),
          Generic("Iso Squat","BJJ", "20s @50%, 10s @80%, 5s @100%"),
          Generic("Iso Row","BJJ", "20s @50%, 10s @80%, 5s @100%"),
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
     'P1 One Wrist Mobility': [Generic("Carpal Tunnel Routine",
          "Theragun","See App")],
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
               Generic("Iso Bridge","BJJ",
                           "20s @50%, 10s @80%, 5s @100%"),
               Generic("Iso Banded Bridge Abduction","BJJ","20s@ 50%, 10s@ 80%, 5s @100%"),
               Generic("Iso Narrow Knees","Hold",
                           "20s @50%, 10s @80%, 5s @100%"),
               Generic("Iso Neck Triceps Extension","BJJ",
                           "20s @50%, 10s @80%, 5s @100%"),
               Generic("Iso Butterfly Crunch","Hold",
                            "20s @50%, 10s @80%, 5s @100%"),
               Generic("Iso Lying Front Raise","BJJ",
                            "20s @50%, 10s @80%, 5s @100%"),
               Generic("Iso Lying Chest Press","BJJ",
                    "20s @50%, 10s @80%, 5s @100%"),
               Generic("Iso Single Foot Row","BJJ",
                    "20s @50%, 10s @80%, 5s @100%")]
}

# Where the magic happens
# this makes it so that this code only runs when this is the main method
if __name__ == "__main__": 
     with open('workout_plan.yaml', 'w') as file:
          yaml.dump(routines, file)

     #index variable is used regardless of wht the user selecs
     index = 0
     # prompt the user to do what is currently scheduled vs selecting one from the 
     # routines which are available
     # demo beep
     
     print("[s] for scheduled")
     print("[a] for ala carte")
     choice = input("select an option: ")
     if choice == "s":
          todays_workouts = scheduled_workout(datetime.date.today())
          todays_reports = [None] * len(todays_workouts)
          for each in todays_workouts:
               todays_reports[index] = do_work(routines,each)
               index = index + 1

     elif choice == "a":
          os.system('clear')
          #print("select a routine from the options below")
          routine_keys = [None] * len(routines)
          for key in routines.keys():
               print(f"[{index}] {key}")
               routine_keys[index] = key
               index = index + 1
          user_input = input("select a routine from the library")
          selected_index = int(user_input)
          todays_workout_name = routine_keys[selected_index]
          print(todays_workout_name)
          report = do_work(routines,todays_workout_name)
     else:
          print ("come on, ya gotta do something today")
