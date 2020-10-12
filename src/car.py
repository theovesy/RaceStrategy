from functions import *
import random

class Car:

    def __init__(self, number, baselaptime):
        self.number = number
        #self.tires = tires
        self.baselaptime = baselaptime #Taken as a basis for the car's laptime
        self.lapcount = 0 #number of laps the car has ran
        self.distance = 0 #distance the car has ran in the LAP
        self.distance_total = 0 #distance the car has ran in the RACE
        self.elapsed_time = 0 #time the car has spent in the RACE
        self.status = "run" 
        self.laptime = self.randomlaptime(self.baselaptime, 0.1)

    def randomlaptime(self, base_laptime, relative_variation):
        absolute_variation = base_laptime*relative_variation
        laptime = random.randrange(int(base_laptime-absolute_variation), int(base_laptime+absolute_variation))
        return laptime

    


    