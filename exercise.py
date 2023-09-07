# define the exercise class

class Exercise:
    # constructor methods
    def __init__(self,name,load):
        self.name = name
        self.load = load

class Time_Based(Exercise):
    # subclass of exercise for time based exercises, like planks or 
    # banded holds
    def __init__(self,name,load,time):
        super().__init__(name,load)
        self.time = time

class Reps_Based(Exercise):
    # subclass of exercise for reps based exercises, such as pushups
    def __init__(self,name,load,reps):
        super().__init__(name,load)
        self.reps = reps

class Generic(Exercise):
    # subclass of exercise for weird exercises that are not strictly time or 
    # strictly reps, such as ramping isometric holds. they take a generic 
    # "instruction" string
    def __init__(self,name,load,instructions):
        super().__init__(name,load)
        self.instructions = instructions