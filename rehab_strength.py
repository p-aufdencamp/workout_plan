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
        #Set 1
        Time_Based("Childs Pose",0,30),
        Reps_Based("Hands on Chair Plank into Bike Pose",0,8),
        Time_Based("Double Leg Squat Jumps",0,30),
        Reps_Based("Pushup Staggered Stance Ball Rolls",0,12),
        Reps_Based("Lateral Step Down",0,10),
        Time_Based("Bear Plank",0,30),

        #Set 2
        Time_Based("Childs Pose",0,30),
        Reps_Based("Hands on Chair Plank into Bike Pose",0,8),
        Time_Based("Double Leg Squat Jumps",0,30),
        Reps_Based("Pushup Staggered Stance Ball Rolls",0,12),
        Reps_Based("Lateral Step Down",0,10),
        Time_Based("Bear Plank",0,30),
        
        #Set 3
        Time_Based("Childs Pose",0,30),
        Reps_Based("Hands on Chair Plank into Bike Pose",0,8),
        Time_Based("Double Leg Squat Jumps",0,30),
        Reps_Based("Pushup Staggered Stance Ball Rolls",0,12),
        Reps_Based("Lateral Step Down",0,10),
        Time_Based("Bear Plank",0,30),
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