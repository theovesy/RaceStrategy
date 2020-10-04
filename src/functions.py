import random

def toMillisecond(time):
    return time*1000

def speed(laptimems, distance):
    return distance/laptimems

def randomlaptime(base_laptime, relative_variation):
    absolute_variation = base_laptime*relative_variation
    laptime = random.randrange(int(base_laptime-absolute_variation), int(base_laptime+absolute_variation))
    return laptime