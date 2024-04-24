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
        # Skater hops 2x30s
        Time_Based("Skater Hops",0,30),
        Time_Based("Rest",0,30),
        Time_Based("Skater Hops",0,20),
        Time_Based("Rest",0,30),

        #Sidestepping with band 3x30s
        Time_Based("Side Stepping w/ Band",0,30),
        Time_Based("Rest",0,30),
        Time_Based("Side Stepping w/ Band",0,30),
        Time_Based("Rest",0,30),
        Time_Based("Side Stepping w/ Band",0,30),
        Time_Based("Rest",0,30),
        
        #Bear plank with chest taps 3x5 on each side
        Reps_Based("Bear Plank w/ Alternating Chest Taps",0,5),
        Time_Based("Rest",0,30),
        Reps_Based("Bear Plank w/ Alternating Chest Taps",0,5),
        Time_Based("Rest",0,30),
        Reps_Based("Bear Plank w/ Alternating Chest Taps",0,5),
        Time_Based("Rest",0,30),

        #SL hopping with assistance 3x15s
        Time_Based("Single Leg Hop w/ Assistance",0,15),
        Time_Based("Rest",0,30),
        Time_Based("Single Leg Hop w/ Assistance",0,15),
        Time_Based("Rest",0,30),
        Time_Based("Single Leg Hop w/ Assistance",0,15),
        Time_Based("Rest",0,30),
        
        #SL squat mini bobs 3x20
        Reps_Based("Single Leg Squat Mini Bobs",0,20),
        Time_Based("Rest",0,30),
        Reps_Based("Single Leg Squat Mini Bobs",0,20),
        Time_Based("Rest",0,30),
        Reps_Based("Single Leg Squat Mini Bobs",0,20),
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