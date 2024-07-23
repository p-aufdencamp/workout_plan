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

            # Jumping Circuit 1of3 : 6 / 12 minutes
            Time_Based("Hop Forward + Backward","Bodyweight",20),
            Time_Based("Rest","None",30),
            Time_Based("Hop Zig Zag","Bodyweight",20),
            Time_Based("Rest","None",30),
            Time_Based("Hop Criss Cross","Bodyweight",20),
            Time_Based("Rest","None",30),
            Time_Based("Alternating Pony Steps","Bodyweight",20),
            Time_Based("Rest","None",30),
            Reps_Based("High Knee Bounds","Bodyweight",12),
            Time_Based("Rest","None",30),
            Reps_Based("Hop Squat","Bodyweight",8),
            Time_Based("Rest","none",30),

            # Jumping Circuit 2of3 : 6 / 18 minutes
            Time_Based("Hop Forward + Backward","Bodyweight",20),
            Time_Based("Rest","None",30),
            Time_Based("Hop Zig Zag","Bodyweight",20),
            Time_Based("Rest","None",30),
            Time_Based("Hop Criss Cross","Bodyweight",20),
            Time_Based("Rest","None",30),
            Time_Based("Alternating Pony Steps","Bodyweight",20),
            Time_Based("Rest","None",30),
            Reps_Based("High Knee Bounds","Bodyweight",12),
            Time_Based("Rest","None",30),
            Reps_Based("Hop Squat","Bodyweight",8),
            Time_Based("Rest","none",30),

            # Jumping Circuit 3of3 : 6 / 24 minutes
            Time_Based("Hop Forward + Backward","Bodyweight",20),
            Time_Based("Rest","None",30),
            Time_Based("Hop Zig Zag","Bodyweight",20),
            Time_Based("Rest","None",30),
            Time_Based("Hop Criss Cross","Bodyweight",20),
            Time_Based("Rest","None",30),
            Time_Based("Alternating Pony Steps","Bodyweight",20),
            Time_Based("Rest","None",30),
            Reps_Based("High Knee Bounds","Bodyweight",12),
            Time_Based("Rest","None",30),
            Reps_Based("Hop Squat","Bodyweight",8),
            Time_Based("Rest","none",30),

            # Isometrics 1 of 4: 4 / 28 minutes
            Time_Based("Forward & Backward Lunges, Right","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),
            Time_Based("Forward & Backward Lunges, Left","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),
            Time_Based("Rolling Planks","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),
            Time_Based("Pushup Planks","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),

            # Isometrics 2 of 4: 4 / 32 minutes
            Time_Based("Forward & Backward Lunges, Right","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),
            Time_Based("Forward & Backward Lunges, Left","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),
            Time_Based("Rolling Planks","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),
            Time_Based("Pushup Planks","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),

            # Isometrics 3 of 4: 4 / 36 minutes
            Time_Based("Forward & Backward Lunges, Right","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),
            Time_Based("Forward & Backward Lunges, Left","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),
            Time_Based("Rolling Planks","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),
            Time_Based("Pushup Planks","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),

            # Isometrics 4 of 4: 4 / 40 minutes
            Time_Based("Forward & Backward Lunges, Right","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),
            Time_Based("Forward & Backward Lunges, Left","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),
            Time_Based("Rolling Planks","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),
            Time_Based("Pushup Planks","Bodyweight",30),
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