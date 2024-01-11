# Author: Phil Aufdencamp

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
        Reps_Based("Half Deadlift w/ Kettlebell",25,15), #Set 1
        Reps_Based("Forward T, Right",0,8),
        Reps_Based("Lunge, Right",0,10),
        Reps_Based("Lateral Step Down, Right",0,10),

        Reps_Based("Half Deadlift w/ Stick","0",15),#Set 2
        Reps_Based("Forward T, Right",0,8),
        Reps_Based("Lunge, Right",0,10),
        Reps_Based("Lateral Step Down, Right",0,10),
        
        Reps_Based("Half Deadlift w/ Stick","0",15), #Set 3
        Reps_Based("Forward T, right",0,8),
        Reps_Based("Lunge, Right",0,10),
        Reps_Based("Lateral Step Down, Right",0,10)
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