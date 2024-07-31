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

            # Jumping Circuit 1of1 : 4 / 10 minutes
            Time_Based("Hop Forward + Backward","Bodyweight",20),
            Time_Based("Rest","None",30),
            Time_Based("Hop Zig Zag","Bodyweight",20),
            Time_Based("Rest","None",30),
            Time_Based("Hop Criss Cross","Bodyweight",20),
            Time_Based("Rest","None",30),
            Time_Based("Alternating Pony Steps","Bodyweight",20),
            Time_Based("Rest","None",30),

            # Plyometrics 1of3 : 3 / 13 minutes
            Reps_Based("High Knee Bounds","Bodyweight",12),
            Time_Based("Rest","None",30),
            Reps_Based("Hop Squat","Bodyweight",8),
            Time_Based("Rest","none",30),
            Reps_Based("Jumping Lunge","Bodyweight",8),

            # Plyometrics 2of3 : 3 / 16 minutes
            Reps_Based("High Knee Bounds","Bodyweight",12),
            Time_Based("Rest","None",30),
            Reps_Based("Hop Squat","Bodyweight",8),
            Time_Based("Rest","none",30),
            Reps_Based("Jumping Lunge","Bodyweight",8),

            # Plyometrics 3of3 : 3 / 19 minutes
            Reps_Based("High Knee Bounds","Bodyweight",12),
            Time_Based("Rest","None",30),
            Reps_Based("Hop Squat","Bodyweight",8),
            Time_Based("Rest","none",30),
            Reps_Based("Jumping Lunge","Bodyweight",8),

            # Lower Body Isometrics 1 of 4: 4 / 23 minutes
            Time_Based("Rear Foot Elevated Split Hold, Left","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),
            Time_Based("Rear Foot Elevated Split Hold, Right","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),
            Reps_Based("Single Leg Skater Squat, Left","Bodyweight",8),
            Time_Based("Rest","Bodyweight",30),
            Reps_Based("Single Leg Skater Squat, Right","Bodyweight",8),
            Time_Based("Rest","Bodyweight",30),

            # Lower Body Isometrics 2 of 4: 4 / 27 minutes
            Time_Based("Rear Foot Elevated Split Hold, Left","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),
            Time_Based("Rear Foot Elevated Split Hold, Right","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),
            Reps_Based("Single Leg Skater Squat, Left","Bodyweight",8),
            Time_Based("Rest","Bodyweight",30),
            Reps_Based("Single Leg Skater Squat, Right","Bodyweight",8),
            Time_Based("Rest","Bodyweight",30),

            # Lower Body Isometrics 3 of 4: 4 / 31 minutes
            Time_Based("Rear Foot Elevated Split Hold, Left","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),
            Time_Based("Rear Foot Elevated Split Hold, Right","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),
            Reps_Based("Single Leg Skater Squat, Left","Bodyweight",8),
            Time_Based("Rest","Bodyweight",30),
            Reps_Based("Single Leg Skater Squat, Right","Bodyweight",8),
            Time_Based("Rest","Bodyweight",30),

            # Lower Body Isometrics 4 of 4: 4 / 35 minutes
            Time_Based("Rear Foot Elevated Split Hold, Left","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),
            Time_Based("Rear Foot Elevated Split Hold, Right","Bodyweight",30),
            Time_Based("Rest","Bodyweight",30),
            Reps_Based("Single Leg Skater Squat, Left","Bodyweight",8),
            Time_Based("Rest","Bodyweight",30),
            Reps_Based("Single Leg Skater Squat, Right","Bodyweight",8),
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