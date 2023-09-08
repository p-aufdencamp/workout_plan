# Author: Phil Aufdencamp
# Main script which you run to do work
# Feature List
# TODO
# (x): Clear the terminal after every user input to make it more focused 
# and easier to stay present
# ( ): print post workout feedback based on the report
# ( ): Add in Mobility Routine to database and to the daily 
# ( ): Have the workout change based on Day of Week
# ( ): Change from phase to phase based on calendar days

# BACKLOG
# ( ): Automate progress across the plan based on compliance and feedback
# ( ): Build a trailing average compliance metric
# ( ): Incorporate a timer function

# import from big python libraries
import yaml
import os 

# do the imports from other classes i've written
from exercise import Time_Based
from exercise import Reps_Based
from exercise import Generic

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
                    Time_Based("Right Plank","Body Weight",45)]
}

with open('workout_plan.yaml', 'w') as file:
    yaml.dump(routines, file)

# define a function to actually do a routine
def do_work(database,workout_name):
    # function to perform a workout located in the database
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

todays_report = do_work(routines,'Phase One Ramping')
print(todays_report)