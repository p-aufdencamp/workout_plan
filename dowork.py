# Author: Phil Aufdencamp
# Main script which you run to do work
# Feature List
# TODO
# ( ): print post workout feedback based on the report 
# (X): Have the workout change based on Day of Week
# ( ): Change from phase to phase based on calendar days
# ( ): do some error handling in the do_work function so that if the 
#      requested routine isn't in the database, it doesn't get mad

# BACKLOG
# ( ): Automate progress across the plan based on compliance and feedback
# ( ): Build a trailing average compliance metric
# ( ): Incorporate a timer function
# ( ): Text based UI for workout browsing, vs doing today's scheduled work

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
    plan = {datetime.date(2023,9,12):'Phase One Banded',
            datetime.date(2023,9,14):'Phase One Ramping',
            datetime.date(2023,9,19):'Phase One Banded',
            datetime.date(2023,9,21):'Phase One Ramping',
            datetime.date(2023,9,26):'Phase One Banded',
            datetime.date(2023,9,28):'Phase One Ramping',
            datetime.date(2023,10,3):'Phase One Banded',
            datetime.date(2023,10,5):'Phase One Ramping',
            datetime.date(2023,10,10):'Phase One Banded',
            datetime.date(2023,10,12):'Phase One Ramping'
            }
    return plan.get(date, None)

# define a function to actually do a routine
def do_work(database,workout_name):
    # function to perform a workout routine located in the database
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
            print(f"Do a {each.name} with {each.load} for {each.reps} reps.")
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
                    Reps_Based("Seated Windshield Wiper, Left","Body Weight",5),
                    Reps_Based("Seated Windshield Wiper, Right","Body Weight",5),
                    Reps_Based("Active Leg Lower, Left","Body Weight",5),
                    Reps_Based("Active Leg Lower, Right","Body Weight",5),
                    Reps_Based("Toe Touch, Raised Heels","Body Weight",10),
                    Reps_Based("Toe Touch, Raised Toes","Body Weight",10)]
}

with open('workout_plan.yaml', 'w') as file:
    yaml.dump(routines, file)

# Walk the user through the workout
todays_workout = scheduled_workout(datetime.date.today())
todays_report = do_work(routines,todays_workout)
print(datetime.date.today())