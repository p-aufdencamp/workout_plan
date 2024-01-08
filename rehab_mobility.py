# Author: Phil Aufdencamp

# This file will store the list of objects which makes up the rehab_mobility 
# routine

# import the exercise classes so that I can make a list populated with those 
# objects

from exercise import Generic
from exercise import Interval
from exercise import Reps_Based
from exercise import Time_Based

rehab_mobility_routine = [Time_Based("Elevated Ankle Dorsiflexion, Right",0,60),
          Time_Based("Plantar Fascia Mobilization",0,60),
          Reps_Based("Heel Raises w/ Counter Support",0,30), 
          Time_Based("Rest",0,30), #Set 1
          Reps_Based("Heel Raises w/ Counter Support",0,30), 
          Time_Based("Rest",0,30), #Set 2
          Reps_Based("Heel Raises w/ Counter Support",0,30)
          ]