# define the exercise class

class Exercise:
    # constructor methods
    def __init__(self,name,load):
        self.name = name
        self.load = load

class Time_Based(Exercise):
    # subclass of exercise for time based exercises, like planks or 
    # banded holds
    def __init__(self,name,load,duration):
        super().__init__(name,load)
        self.duration = duration

class Reps_Based(Exercise):
    # subclass of exercise for reps based exercises, such as pushups
    def __init__(self,name,load,reps):
        super().__init__(name,load)
        self.reps = reps

class Generic(Exercise):
    # subclass of exercise for weird exercises that are not strictly time or 
    # strictly reps, such as referencing predefined, external routines such as theragun 
    # routines or trainer work. they take a generic "instruction" string
    def __init__(self,name,load,instructions):
        super().__init__(name,load)
        self.instructions = instructions

class Interval(Exercise):
    # subclass of exercise for interval based exercises, such as ramping, holds.
    # These intervals don't have to be equal
    # Instuctions and times are both lists of equal length
    def __init__(self,name,instructions,times):
        super().__init__(name,load)
        self.instructions = instructions
        self.times = times