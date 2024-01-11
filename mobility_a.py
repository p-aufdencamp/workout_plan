################################################################################
# Author: Phil Aufdencamp

# This file will store the list of objects which makes up the mobility_a routine

# import the exercise classes so that I can make a list populated with those 
# objects

from exercise import Generic
from exercise import Interval
from exercise import Reps_Based
from exercise import Time_Based

def get_mobility_a_routine(settings):
    
    if settings['selected_user'] == "p":
        routine = [Time_Based("Forward Fold",0,60),
          Time_Based("Bow Stretch, Left",0,60),
          Time_Based("Bow Stretch, Right",0,60),
          Time_Based("Lying Spine Twist, Left",0,60),
          Time_Based("Lying Spine Twist, Right",0,60),
          Reps_Based("MacKenzie Extensions",0,10)]
        
    elif settings['selected_user'] == "c":
        routine = [
            Generic("Theragun: Shoulder Routine",0,"See Theragun App")]
    else:
        routine = Generic("Yoga",0,"30 minutes worth")
    
    return routine