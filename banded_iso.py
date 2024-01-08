# Author: Phil Aufdencamp

# This file will store the list of objects which makes up the banded iso
# routine

# import the exercise classes so that I can make a list populated with those 
# objects

from exercise import Generic
from exercise import Interval
from exercise import Reps_Based
from exercise import Time_Based

banded_iso_routine = [Time_Based("Plank on Elbows",0,45),
          Reps_Based("Lying Side Leg Raise, Left","Bodyweight",10),
          Reps_Based("Lying Side Leg Leg, Right","Bodyweight",10),
          Time_Based("Banded Bridge","Medium Band",45),
          Time_Based("Banded Narrow Knees","Light Band",45),
          Time_Based("Banded Back Neck Hold","Light Band",45),
          Time_Based("Banded Front Neck Hold","Light Band",45),
          Time_Based("Banded Front Raise","Light Band",45),
          Time_Based("Banded Chest Press","Medium Heavy Band",45),
          Time_Based("Banded Row","Medium Heavy Band",45),
          Time_Based("Left Plank","Body Weight",20),
          Time_Based("Right Plank","Body Weight",20)]