# Author: Phil Aufdencamp
# Main script which you run to do work
# Feature List
# TODO
# ( ): print post workout feedback based on the report 
# ( ): Change from phase to phase based on calendar days
# ( ): do some error handling in the do_work function so that if the 
#      requested routine isn't in the database, it doesn't get mad
# (X): Text based UI for workout browsing, vs doing today's scheduled work

# BACKLOG
# ( ): Automate progress across the plan based on compliance and feedback,
#      maybe with an index variable
# ( ): Build a trailing average compliance metric
# ( ): Incorporate a timer function
# ( ): Do some error handling in the scheduled workout function so that if 
#       today doesn't have a scheduled workout, it doesn't get mad


# import from big python libraries
import yaml
import os 
import datetime

# do the imports from other classes i've written
from exercise import Time_Based
from exercise import Reps_Based
from exercise import Generic


def scheduled_workout(date):
    # function which will return a routine based on the date provided and the 
    # plan. Eventually this is where the smarts for progressing and responding
    # to skipped workouts will reside

    #starting with just hard coded plan and will go from there.
    plan = {datetime.date(2023,9,12):['Phase One Hip Mobility',
                                      'Phase One Banded'],
        datetime.date(2023,9,14):['Phase One Hip Mobility',
                                      'Phase One Ramping'],
        datetime.date(2023,9,15):['Phase One Hip Mobility'],
        datetime.date(2023,9,18):['Phase One Wrist Mobility',
                                  'Phase One Shoulder Mobility'],
        datetime.date(2023,9,19):['Phase One Hip Mobility',
                                      'Phase One Banded'],
        datetime.date(2023,9,20):['Phase One Wrist Mobility',
                                      'Phase One Shoulder Mobility'],
        datetime.date(2023,9,21):['Phase One Hip Mobility',
                                      'Phase One Ramping'],
        datetime.date(2023,9,22):['Phase One Wrist Mobility',
                                      'Phase One Shoulder Mobility'],
        datetime.date(2023,9,25):['Phase One Wrist Mobility',
                                      'Phase One Shoulder Mobility'],
        datetime.date(2023,9,26):['Phase One Hip Mobility',
                                      'Phase One Banded'],
        datetime.date(2023,9,27):['Phase One Wrist Mobility',
                                      'Phase One Shoulder Mobility'],
        datetime.date(2023,9,28):['Phase One Hip Mobility',
                                      'Phase One Ramping'],
        datetime.date(2023,9,29):['Phase One Wrist Mobility',
                                      'Phase One Shoulder Mobility'],
        datetime.date(2023,10,2):['Phase One Wrist Mobility',
                                      'Phase One Shoulder Mobility'],
        datetime.date(2023,10,3):['Phase One Hip Mobility',
                                      'Phase One Banded'],
        datetime.date(2023,10,4):['Phase One Hip Mobility'],
        datetime.date(2023,10,5):['Phase One Hip Mobility',
                                      'Phase One Ramping'],
        datetime.date(2023,10,6):['Phase One Wrist Mobility',
                                      'Phase One Shoulder Mobility'],
        datetime.date(2023,10,9):['Phase One Wrist Mobility',
                                      'Phase One Shoulder Mobility'],
        datetime.date(2023,10,10):['Phase One Hip Mobility',
                                       'Phase One Banded'],
        datetime.date(2023,10,11):['Phase One Hip Mobility'],
        datetime.date(2023,10,12):['Phase One Hip Mobility',
                                       'Phase One Ramping'],
        datetime.date(2023,10,13):['Phase One Wrist Mobility',
                                      'Phase One Shoulder Mobility'],
        datetime.date(2023,10,30):['P1 Recovery'],
        datetime.date(2023,10,31):['P1 Recovery'],
        datetime.date(2023,11,1):['P1 Recovery','P1 Banded, Modified'],
        datetime.date(2023,11,2):['P1 Recovery'],
        datetime.date(2023,11,3):['P1 Recovery','P1 Ramping, Modified'],
        datetime.date(2023,11,4):['P1 Recovery'],
        datetime.date(2023,11,5):['P1 Recovery'],
        datetime.date(2023,11,6):['P1 Recovery','P1 Banded, Modified'],
        datetime.date(2023,11,7):['P1 Recovery'],
        datetime.date(2023,11,8):['P1 Recovery','P1 Ramping, Modified'],
        datetime.date(2023,11,9):['P1 Recovery'], 
        datetime.date(2023,11,10):['P1 Recovery','P1 Banded, Modified'],
        datetime.date(2023,11,11):['P1 Recovery'],
        datetime.date(2023,11,12):['P1 Recovery'],
        datetime.date(2023,11,13):['P1 Recovery','P1 Ramping, Modified'],
        datetime.date(2023,11,14):['P1 Recovery'],
        datetime.date(2023,11,15):['P1 Recovery','P1 Banded, Modified'],
        datetime.date(2023,11,16):['P1 Recovery'],
        datetime.date(2023,11,17):['P1 Recovery','P1 Ramping, Modified'],
        datetime.date(2023,11,18):['P1 Recovery'],
        datetime.date(2023,11,19):['P1 Recovery'],
        datetime.date(2023,11,20):['P1 Recovery','P1 Banded, Modified'],
        datetime.date(2023,11,21):['P1 Recovery']
        }
    return plan.get(date, None)

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
               print(f"Do a {each.name} with {each.load} for {each.time} seconds.")
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
     'Phase One Banded': [Time_Based("Plank","Bodyweight",45),
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
     'Phase One Ramping': [Time_Based("Plank","Bodyweight",45),
                   Reps_Based("Lying Side Leg Raise, Left","Bodyweight",10),
                   Reps_Based("Lying Side Leg Leg, Right","Bodyweight",10),
                   Generic("Iso Bridge","BJJ",
                           "20s @50%, 10s @80%, 5s @100%"),
                   Generic("Iso Narrow Knees","Hold",
                           "20s @50%, 10s @80%, 5s @100%"),
                    Generic("Iso Neck Triceps Extension","BJJ",
                           "20s @50%, 10s @80%, 5s @100%"),
                    Generic("Iso Butterfly Crunch","Hold",
                            "20s @50%, 10s @80%, 5s @100%"),
                    Generic("Iso Front Raise","BJJ",
                            "20s @50%, 10s @80%, 5s @100%"),
                    Generic("Iso Deadlift","BJJ",
                            "20s @50%, 10s @80%, 5s @100%"),
                    Generic("Iso Chest Press","BJJ",
                            "20s @50%, 10s @80%, 5s @100%"),
                    Generic("Iso Squat","BJJ",
                            "20s @50%, 10s @80%, 5s @100%"),
                    Generic("Iso Row","BJJ",
                            "20s @50%, 10s @80%, 5s @100%"),
                    Time_Based("Left Plank","Body Weight",45),
                    Time_Based("Right Plank","Body Weight",45)],
     'Phase One Hip Mobility': [Generic("Cycling Recovery","Theragun","See App"),
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
     'Phase One Wrist Mobility': [Generic("Carpal Tunnel Routine","Theragun","See App")],
     'Phase One Shoulder Mobility': [Generic("Shoulders","Theragun","See App"),
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
     'P1 Recovery': [Reps_Based("Ankle Vertical Flexion, Right",0,10),
                        Reps_Based("Ankle Circles, Right, CW",0,30),
                        Reps_Based("Ankle Circles, Right, CCW",0,30),
                        Time_Based("Ankle Dorsiflexion, Right",0,60),
                        Reps_Based("Ankle Vertical Flexion, Left",0,10),
                        Reps_Based("Ankle Circles, Left, CW",0,30),
                        Reps_Based("Ankle Circles, Left, CCW",0,30),
                        Time_Based("Ankle Dorsiflexion, Left",0,60),
                        Time_Based("Forward Fold",0,60),
                        Reps_Based("Mackenzie Extensions",0,15),
                        Time_Based("Bow Stretch, Left",0,60),
                        Time_Based("Bow Stretch, Right",0,60),
                        Time_Based("Lying Spine Twist, Left",0,60),
                        Time_Based("Lying Spine Twist, Right",0,60),
                        Reps_Based("Lying Vertical Leg Raise, Right",10,10),
                        Reps_Based("Lying Vertidcal Leg Raise, Left",10,10),
                        Reps_Based("Lying Side Leg Raise, Right",10,10),
                        Reps_Based("Lying Knee Flexion, Right",10,10),
                        Reps_Based("Lying Glute Raise, Right",10,10),
                        Reps_Based("Lying Glute Raise, Left",10,10),
                        Reps_Based("Lying Knee Flexion, Left",10,10),
                        Reps_Based("Lying Side Leg Raise, Left",10,10)],
     'P1 Banded, Modified': [Time_Based("Kneeling Plank",0,45),
                  Reps_Based("Bicycle Crunch",0,10),
                  Time_Based("Lying Banded Front Raise","Light Band",45),
                  Time_Based("Lying Banded Chest Press","Medium Heavy Band",45),
                  Time_Based("Banded Row, Single Foot","Medium Heavy Band",45)],
     'P1 Ramping, Modified': [Time_Based("Kneeling Plank",0,45),
                   Reps_Based("Bicycle Crunch",0,10),
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
#this makes it so that this code only runs when this is the main method
if __name__ == "__main__": 
     with open('workout_plan.yaml', 'w') as file:
          yaml.dump(routines, file)

     #index variable is used regardless of wht the user selecs
     index = 0
     # prompt the user to do what is currently scheduled vs selecting one from the 
     # routines which are available
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
