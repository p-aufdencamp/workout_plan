# Author: Phil Aufdencamp

# (X) Add back in Squat & Deadlift
# (X) Combine Front Plank and Chest Press into one Isometric Pushup

# This file will store the list of objects which makes up the banded iso
# routine

# import the exercise classes so that I can make a list populated with those 
# objects

from exercise import Generic
from exercise import Interval
from exercise import Reps_Based
from exercise import Time_Based

def get_strength_a_routine(settings):
    
    if settings['selected_user'] == "p":
        # Isometric Routine
        routine = [
            #Warm Up: 6 minutes
            Time_Based("Knee to Chest Alternating","Body weight",60),
            Time_Based("Quad Stretch, Left","Bodyweight",60),
            Time_Based("Quad Stretch, Right","Bodyweight",60),
            Time_Based("Hamstring Sweeps, Alternating", "Bodyweight",60),
            Time_Based("Side Lunge, Alternating","Bodyweight",60),
            Time_Based("Lunge w/ Twist, Alternating","Body",60),

            # Plyometrics 1of3 : +5 = 11 minutes
            Reps_Based("High Knee Bounds, Left","Bodyweight",12),
            Time_Based("Rest","None",30),
            Reps_Based("High Knee Bounds, Right","Bodyweight, Assist if needed",12),
            Time_Based("Rest","None",30),
            Reps_Based("Hop Squat","Bodyweight",12),
            Time_Based("Rest","none",30),
            Reps_Based("Jumping Lunge Left","Bodyweight",12),
            Time_Based("Rest","none",30),
            Reps_Based("Jumping Lunge Right","Bodyweight",12),
            Time_Based("Rest","none",30),

            # Plyometrics 2of3 : +5 = 16 minutes
            Reps_Based("High Knee Bounds, Left","Bodyweight",12),
            Time_Based("Rest","None",30),
            Reps_Based("High Knee Bounds, Right","Bodyweight, Assist if needed",12),
            Time_Based("Rest","None",30),
            Reps_Based("Hop Squat","Bodyweight",12),
            Time_Based("Rest","none",30),
            Reps_Based("Jumping Lunge Left","Bodyweight",12),
            Time_Based("Rest","none",30),
            Reps_Based("Jumping Lunge Right","Bodyweight",12),
            Time_Based("Rest","none",30),

            # Plyometrics 3of3 : +5 = 21 minutes
            Reps_Based("High Knee Bounds, Left","Bodyweight",12),
            Time_Based("Rest","None",30),
            Reps_Based("High Knee Bounds, Right","Bodyweight, Assist if needed",12),
            Time_Based("Rest","None",30),
            Reps_Based("Hop Squat","Bodyweight",12),
            Time_Based("Rest","none",30),
            Reps_Based("Jumping Lunge Left","Bodyweight",12),
            Time_Based("Rest","none",30),
            Reps_Based("Jumping Lunge Right","Bodyweight",12),
            Time_Based("Rest","none",30),

            # Lower Body Bodyweight 1 of 1: +3 = 24 minutes
            Reps_Based("Left Leg Elevated Hamstring Bridge, 10s + 5 reps","Bodyweight",3),
            Time_Based("Rest","Bodyweight",30),
            Reps_Based("Left Leg Elevated Hamstring Bridge, 10s + 5 reps","Bodyweight",3),
            Time_Based("Rest","Bodyweight",30),
            Reps_Based("Left Leg Elevated Hamstring Bridge, 10s + 5 reps","Bodyweight",3),
            Time_Based("Rest","Bodyweight",30)
            
        ]
        
    elif settings['selected_user'] == "c":
        routine = [Reps_Based("Pushups",0,15),#Set 1
            Reps_Based("Military Press","25lbs ea",10),
            Time_Based("Rest",0,60),

            Reps_Based("Pushups",0,15),#Set 2
            Reps_Based("Military Press","25lbs ea",10),
            Time_Based("Rest",0,60),

            Reps_Based("Pushups",0,15),#Set 3
            Reps_Based("Military Press","25lbs ea",10),
            Time_Based("Rest",0,60)
        ]
    else:
         routine = [Reps_Based("Pushups",0,15),#Set 1
            Reps_Based("Military Press","25lbs ea",10),
            Time_Based("Rest",0,60),

            Reps_Based("Pushups",0,15),#Set 2
            Reps_Based("Military Press","25lbs ea",10),
            Time_Based("Rest",0,60),

            Reps_Based("Pushups",0,15),#Set 3
            Reps_Based("Military Press","25lbs ea",10),
            Time_Based("Rest",0,60)]
    return routine