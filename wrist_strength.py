# Author: Phil Aufdencamp

# This file will store the list of objects which makes up the wrist strength 
# routine

# import the exercise classes so that I can make a list populated with those 
# objects

from exercise import Generic
from exercise import Interval
from exercise import Reps_Based
from exercise import Time_Based

def get_wrist_strength_routine(settings):
    
    if settings['selected_user'] == "p":
        routine = [Reps_Based("Wrist Extensions, Left", 6,10), #Set 1
        Reps_Based("Wrist Extensions, Right", 6,10),
        Time_Based("Rest",0,15),

        Reps_Based("Wrist Extensions, Left", 6,10), # Set 2
        Reps_Based("Wrist Extensions, Right", 6,10),
        Time_Based("Rest",0,15),

        Reps_Based("Wrist Extensions, Left", 6,10), # Set 3
        Reps_Based("Wrist Extensions, Right", 6,10),
        Time_Based("Rest",0,15),

        Reps_Based("Hammer Twist, Left",6,10), # Set 1
        Reps_Based("Hammer Twist, Right",6,10),
        Time_Based("Rest",0,15),

        Reps_Based("Hammer Twists, Left",6,10), # Set 2
        Reps_Based("Hammer Twist, Right",6,10),
        Time_Based("Rest",0,15),

        Reps_Based("Hammer Twists, Left",6,10), # Set 3
        Reps_Based("Hammer Twist, Right",6,10),
        Time_Based("Rest",0,15)
        ]
    elif settings['selected_user'] == "c":
        routine = [Reps_Based("Wrist Extensions, Left", 6,10), #Set 1
        Reps_Based("Wrist Extensions, Right", 6,10),
        Time_Based("Rest",0,15),

        Reps_Based("Wrist Extensions, Left", 6,10), # Set 2
        Reps_Based("Wrist Extensions, Right", 6,10),
        Time_Based("Rest",0,15),

        Reps_Based("Wrist Extensions, Left", 6,10), # Set 3
        Reps_Based("Wrist Extensions, Right", 6,10),
        Time_Based("Rest",0,15),

        Reps_Based("Hammer Twist, Left",6,10), # Set 1
        Reps_Based("Hammer Twist, Right",6,10),
        Time_Based("Rest",0,15),

        Reps_Based("Hammer Twists, Left",6,10), # Set 2
        Reps_Based("Hammer Twist, Right",6,10),
        Time_Based("Rest",0,15),

        Reps_Based("Hammer Twists, Left",6,10), # Set 3
        Reps_Based("Hammer Twist, Right",6,10),
        Time_Based("Rest",0,15)
        ]
    else:
        routine = [Reps_Based("Wrist Extensions, Left", 6,10), #Set 1
        Reps_Based("Wrist Extensions, Right", 6,10),
        Time_Based("Rest",0,15),

        Reps_Based("Wrist Extensions, Left", 6,10), # Set 2
        Reps_Based("Wrist Extensions, Right", 6,10),
        Time_Based("Rest",0,15),

        Reps_Based("Wrist Extensions, Left", 6,10), # Set 3
        Reps_Based("Wrist Extensions, Right", 6,10),
        Time_Based("Rest",0,15),

        Reps_Based("Hammer Twist, Left",6,10), # Set 1
        Reps_Based("Hammer Twist, Right",6,10),
        Time_Based("Rest",0,15),

        Reps_Based("Hammer Twists, Left",6,10), # Set 2
        Reps_Based("Hammer Twist, Right",6,10),
        Time_Based("Rest",0,15),

        Reps_Based("Hammer Twists, Left",6,10), # Set 3
        Reps_Based("Hammer Twist, Right",6,10),
        Time_Based("Rest",0,15)
        ]
    return routine