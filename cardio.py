################################################################################
# Author: Phil Aufdencamp

# This file will store the list of objects which makes up the cardio routine

# import the exercise classes so that I can make a list populated with those 
# objects

from exercise import Generic
from exercise import Interval
from exercise import Reps_Based
from exercise import Time_Based

def get_cardio_routine(settings):
    
    if settings['selected_user'] == "p":
        routine = [Generic("Trainerroad Workout",0,"Open App")]
        
    elif settings['selected_user'] == "c":
        routine = [
            Generic("Peloton Workout",0,"See Peloton App")]
    else:
        routine = Generic("Brisk Walk",0,"30 minutes worth")
    
    return routine