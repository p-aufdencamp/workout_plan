# Author: Phil Aufdencamp

# ( ) Combine plank and chest press into one isometric pushup
# ( ) Add back in the squats and deadlifts but take off the final break it strength for now

# This file will store the list of objects which makes up the ramping iso 
# routine

# import the exercise classes so that I can make a list populated with those 
# objects

from exercise import Generic
from exercise import Interval
from exercise import Reps_Based
from exercise import Time_Based

def get_strength_b_routine(settings):
    
    if settings['selected_user'] == "p":
        # isometric ramping isos
        routine = [
          Reps_Based("Lying Side Leg Raise, Left","Bodyweight",10),
          Reps_Based("Lying Side Leg Leg, Right","Bodyweight",10),
          Interval("Iso Bridge (No max)",["Press", "Press"],
                           ["50%","80%"],[20,10]),
          Interval("Iso Narrow Knees",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Neck Triceps Extension",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Butterfly Crunch",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Front Raise",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Deadlift (No Max)",["Press", "Press"],
                           ["50%","80%"],[20,10]),
          Interval("Iso Push Up",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Squat (No Max)",["Press", "Press"],
                           ["50%","80%"],[20,10]),
          Interval("Iso Row",["Press", "Press", "Press"],
                           ["50%","80%","110%"],[20,10,5]),
          Time_Based("Left Plank","Body Weight",45),
          Time_Based("Right Plank","Body Weight",45)]
        
    elif settings['selected_user'] == "c":
        routine = [Reps_Based("Body Weight Squat",0,15),#Set 1
            Reps_Based("Suitcase Deadlifts","25lbs ea",10),
            Time_Based("Rest",0,60),

            Reps_Based("Body Weight Squat",0,15),#Set 2
            Reps_Based("Suitcase Deadlifts","25lbs ea",10),
            Time_Based("Rest",0,60),

            Reps_Based("Body Weigh Squat",0,15),#Set 3
            Reps_Based("Suitcase Deadlifts","25lbs ea",10),
            Time_Based("Rest",0,60)
        ]
    else:
         routine = [Reps_Based("Body Weight Squat",0,15),#Set 1
            Reps_Based("Suitcase Deadlifts","25lbs ea",10),
            Time_Based("Rest",0,60),

            Reps_Based("Body Weight Squat",0,15),#Set 2
            Reps_Based("Suitcase Deadlifts","25lbs ea",10),
            Time_Based("Rest",0,60),

            Reps_Based("Body Weigh Squat",0,15),#Set 3
            Reps_Based("Suitcase Deadlifts","25lbs ea",10),
            Time_Based("Rest",0,60)]

    return routine

ramping_iso_routine = [Time_Based("Plank on Elbows",0,45),
          Reps_Based("Lying Side Leg Raise, Left","Bodyweight",10),
          Reps_Based("Lying Side Leg Leg, Right","Bodyweight",10),
          Interval("Iso Bridge",["Press", "Press", "Press"],
                         ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Narrow Knees",["Press", "Press", "Press"],
                         ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Neck Triceps Extension",["Press","Press","Press"],
                         ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Butterfly Crunch",["Press", "Press", "Press"],
                         ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Front Raise",["Press", "Press", "Press"],
                         ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Chest Press",["Press", "Press", "Press"],
                         ["50%","80%","110%"],[20,10,5]),
          Interval("Iso Row",["Press", "Press", "Press"],
                         ["50%","80%","110%"],[20,10,5]),
          Time_Based("Left Plank","Body Weight",20),
          Time_Based("Right Plank","Body Weight",20)]