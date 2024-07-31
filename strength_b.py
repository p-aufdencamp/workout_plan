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
        # Crawling Routine
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

            # Upper Body Isometrics 1 of 4 : 4 / 23 minutes
            Time_Based("Hear Crawl Weight Shifts","Bodyweight",30),
            Time_Based("Rest","None",30),
            Time_Based("Shoulder Taps","Body weight",30),
            Time_Based("Rest","None",30),
            Time_Based("Cross Body Toe Taps","Body weight",30),
            Time_Based("Rest","None",30),
            Time_Based("4-Way Pushups","Body weight",30),
            Time_Based("Rest","None",30),

            # Upper Body Isometrics 2 of 4 : 4 / 27 minutes
            Time_Based("Hear Crawl Weight Shifts","Bodyweight",30),
            Time_Based("Rest","None",30),
            Time_Based("Shoulder Taps","Body weight",30),
            Time_Based("Rest","None",30),
            Time_Based("Cross Body Toe Taps","Body weight",30),
            Time_Based("Rest","None",30),
            Time_Based("4-Way Pushups","Body weight",30),
            Time_Based("Rest","None",30),

            # Upper Body Isometrics 3 of 4 : 4 / 31 minutes
            Time_Based("Hear Crawl Weight Shifts","Bodyweight",30),
            Time_Based("Rest","None",30),
            Time_Based("Shoulder Taps","Body weight",30),
            Time_Based("Rest","None",30),
            Time_Based("Cross Body Toe Taps","Body weight",30),
            Time_Based("Rest","None",30),
            Time_Based("4-Way Pushups","Body weight",30),
            Time_Based("Rest","None",30),

            # Upper Body Isometrics 4 of 4 : 4 / 35 minutes
            Time_Based("Hear Crawl Weight Shifts","Bodyweight",30),
            Time_Based("Rest","None",30),
            Time_Based("Shoulder Taps","Body weight",30),
            Time_Based("Rest","None",30),
            Time_Based("Cross Body Toe Taps","Body weight",30),
            Time_Based("Rest","None",30),
            Time_Based("4-Way Pushups","Body weight",30),
            Time_Based("Rest","None",30)
        ]

        
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