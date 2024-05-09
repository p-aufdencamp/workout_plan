# Author: Phil Aufdencamp
# Update 2/10/24:

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

        #SL hopping with assistance 3x15s
        Time_Based("Single Leg Hop",0,20),
        Time_Based("Rest",0,30),
        Time_Based("Single Leg Hop",0,20),
        Time_Based("Rest",0,30),
        Time_Based("Single Leg Hop",0,20),
        Time_Based("Rest",0,30),
        
        #Lateral Lunge 
        Reps_Based("Lateral Lunge Right",0,8),
        Time_Based("Rest",0,30),
        Reps_Based("Lateral Lunge Right",0,8),
        Time_Based("Rest",0,30),
        Reps_Based("Lateral Lunge Right",0,8),
        Time_Based("Rest",0,30)
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