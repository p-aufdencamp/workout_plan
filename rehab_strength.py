# Author: Phil Aufdencamp
# Update 1/21/24:
# New workout is 
# 3 sets of 
# ( )6x Single Leg Sit to Stand
# ( )12x Standing Clam with Resistance Loop, Left Leg Down
# ( )10x Upright Side Lunge
# ( )30s single leg balance on foam pad
# ( )10x Alternating Bird Dogs, knees on foam pad

# This file will store the list of objects which makes up the rehab_strength
# routine

# import the exercise classes so that I can make a list populated with those 
# objects

from exercise import Generic
from exercise import Interval
from exercise import Reps_Based
from exercise import Time_Based

def get_rehab_strength_routine(settings):
    
    if settings['selected_user'] == "p":
        routine = [
        #Set 1
        Reps_Based("Single Leg Sit to Stand, Arms Extended ",0,6), 
        Reps_Based("Standing Clam w/ Reistance Band, Right","vLight",12),
        Reps_Based("Standing Clam w/ Reistance Band, Left","vLight",12),
        Reps_Based("Upright Side Lunge, Right",0,10),
        Reps_Based("Upright Side Lunge, Left",0,10),
        Time_Based("Single Leg Balance on Foam Pad, Right",0,30),
        Reps_Based("Alternating Bird Dogs",0,10),

        #Set 2
        Reps_Based("Single Leg Sit to Stand, Arms Extended ",0,6), 
        Reps_Based("Standing Clam w/ Reistance Band, Right","vLight",12),
        Reps_Based("Standing Clam w/ Reistance Band, Left","vLight",12),
        Reps_Based("Upright Side Lunge, Right",0,10),
        Reps_Based("Upright Side Lunge, Left",0,10),
        Time_Based("Single Leg Balance on Foam Pad, Right",0,30),
        Reps_Based("Alternating Bird Dogs",0,10),
        
        #Set 3
        Reps_Based("Single Leg Sit to Stand, Arms Extended ",0,6), 
        Reps_Based("Standing Clam w/ Reistance Band, Right","vLight",12),
        Reps_Based("Standing Clam w/ Reistance Band, Left","vLight",12),
        Reps_Based("Upright Side Lunge, Right",0,10),
        Reps_Based("Upright Side Lunge, Left",0,10),
        Time_Based("Single Leg Balance on Foam Pad, Right",0,30),
        Reps_Based("Alternating Bird Dogs",0,10),
        ]
    elif settings['selected_user'] == "c":
        routine = [
        Reps_Based("Pushups",0,10),
        Reps_Based("Bodyweight Squat",0,10)
        ]
    else:
        routine = [
        Reps_Based("Pushups",0,5),
        Reps_Based("Kettlebell Swings",25,15)
        ]

    return routine