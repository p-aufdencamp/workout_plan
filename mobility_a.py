# Author: Phil Aufdencamp

# This file will store the list of objects which makes up the mobility_a routine

# import the exercise classes so that I can make a list populated with those 
# objects

from exercise import Generic
from exercise import Interval
from exercise import Reps_Based
from exercise import Time_Based

mobility_a_routine = [Time_Based("Forward Fold",0,60),
          Time_Based("Bow Stretch, Left",0,60),
          Time_Based("Bow Stretch, Right",0,60),
          Time_Based("Lying Spine Twist, Left",0,60),
          Time_Based("Lying Spine Twist, Right",0,60),
          Reps_Based("MacKenzie Extensions",0,10)]