from functions import *

class Car:

    def __init__(self, number, baselaptime):
        self.number = number
        #self.tires = tires
        self.baselaptime = baselaptime
        self.lapcount = 0
        self.distance = 0
        self.elapsed_time = 0
        self.status = "run"
        self.laptime = randomlaptime(self.baselaptime, 0.1)


    


    