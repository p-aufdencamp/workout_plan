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
        #Set -1
        Reps_Based("Single Leg Heel Raise, straight leg, keep ankle out",0,20),
        Time_Based("Rest",0,30),
        Reps_Based("Single Leg Heel Raise, knee Bent, keep ankle out",0,20),
        Time_Based("Rest",0,30),

        #Set 0
        Reps_Based("Single Leg Heel Raise, keep ankle out",0,20),
        Time_Based("Rest",0,30),
        Reps_Based("Single Leg Heel Raise, knee Bent, keep ankle out",0,20),
        Time_Based("Rest",0,30),
        
        # Set 1
        Reps_Based("Double Leg Decline Squat w/ weight",30,12),
        Reps_Based("Single Leg Squat Heel Elevated",0,10),
        Time_Based("Double Leg Squat Jumps",0,20),
        Reps_Based("6in Lateral Step down w/ Arch Lift",0,12),

        #Set 2
        Reps_Based("Double Leg Decline Squat w/ weight",30,12),
        Reps_Based("Single Leg Squat Heel Elevated",0,10),
        Time_Based("Double Leg Squat Jumps",0,20),
        Reps_Based("6in Lateral Step down w/ Arch Lift",0,12),
        
        #Set 3
        Reps_Based("Double Leg Decline Squat w/ weight",30,12),
        Reps_Based("Single Leg Squat Heel Elevated",0,10),
        Time_Based("Double Leg Squat Jumps",0,20),
        Reps_Based("6in Lateral Step down w/ Arch Lift",0,12),

        # Bonus Set
        Reps_Based("Double Leg Decline Squat w/ weight",30,12)
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