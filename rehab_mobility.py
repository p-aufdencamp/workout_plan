# Author: Phil Aufdencamp
################################################################################
# Updates 1/21/24
# Changed from 4x10 Heel Raises to 3x15 Heel Raises, with rests in between

# This file will store the list of objects which makes up the rehab_mobility 
# routine

# import the exercise classes so that I can make a list populated with those 
# objects

from exercise import Generic
from exercise import Interval
from exercise import Reps_Based
from exercise import Time_Based

# function which will return the appropriate rehab mobility routine per user
def get_rehab_mobility_routine(settings):

    phil_rehab_mobility_routine = [
        Reps_Based("Single Leg Heel Raise, Right",0,20),
        Time_Based("Rest",0,30),
        Reps_Based("Single Leg Heel Raise, Right",0,20),
        Time_Based("Rest",0,30),
        Reps_Based("Single Leg Heel Raise, Right",0,20),
        Time_Based("Rest",0,30)
        ]
    
    claudi_rehab_mobility_routine = [
        Generic("Theragun: Calf & Shin Routine",0,"See Theragun App")
        ]
    
    default_rehab_mobility_routine = [
        Generic("Yoga",0,"30 minutes worth")
        ]
    
    if settings['selected_user'] == "p":
        return phil_rehab_mobility_routine
    elif settings['selected_user'] == "c":
        return claudi_rehab_mobility_routine
    else:
        return default_rehab_mobility_routine


