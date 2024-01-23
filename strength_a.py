# Author: Phil Aufdencamp

# (X) Add back in Squat & Deadlift
# (X) Combine Front Plank and Chest Press into one Isometric Pushup

# This file will store the list of objects which makes up the banded iso
# routine

# import the exercise classes so that I can make a list populated with those 
# objects

from exercise import Generic
from exercise import Interval
from exercise import Reps_Based
from exercise import Time_Based

def get_strength_a_routine(settings):
    
    if settings['selected_user'] == "p":
        # Banded Iso Routine
        routine = [
        Reps_Based("Lying Side Leg Raise, Left","Bodyweight",10),
        Reps_Based("Lying Side Leg Leg, Right","Bodyweight",10),
        Time_Based("Banded Bridge","Medium Band",45),
        Time_Based("Banded Narrow Knees","Light Band",45),
        Time_Based("Banded Back Neck","Light Band",45),
        Time_Based("Banded Back Neck Hold","Light Band",45),
        Time_Based("Banded Front Raise","Light Band",45),
        Time_Based("Banded Deadlift","Medium Heavy Band",45),
        Time_Based("Isometric Pushup","Light Band",45),
        Time_Based("Banded Squat","Light Band",45),
        Time_Based("Banded Row","Medium Heavy Band",45),
        Time_Based("Left Plank","Body Weight",45),
        Time_Based("Right Plank","Body Weight",45)]
        
    elif settings['selected_user'] == "c":
        routine = [Reps_Based("Pushups",0,15),#Set 1
            Reps_Based("Military Press","25lbs ea",10),
            Time_Based("Rest",0,60),

            Reps_Based("Pushups",0,15),#Set 2
            Reps_Based("Military Press","25lbs ea",10),
            Time_Based("Rest",0,60),

            Reps_Based("Pushups",0,15),#Set 3
            Reps_Based("Military Press","25lbs ea",10),
            Time_Based("Rest",0,60)
        ]
    else:
         routine = [Reps_Based("Pushups",0,15),#Set 1
            Reps_Based("Military Press","25lbs ea",10),
            Time_Based("Rest",0,60),

            Reps_Based("Pushups",0,15),#Set 2
            Reps_Based("Military Press","25lbs ea",10),
            Time_Based("Rest",0,60),

            Reps_Based("Pushups",0,15),#Set 3
            Reps_Based("Military Press","25lbs ea",10),
            Time_Based("Rest",0,60)]
    return routine