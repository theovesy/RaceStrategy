import random 
import time

def toMillisecond(time):
    return time*1000

def speed(laptimems, distance):
    return distance/laptimems

def randomlaptime(base_laptime, relative_variation):
    absolute_variation = base_laptime*relative_variation
    laptime = random.randrange(int(base_laptime-absolute_variation), int(base_laptime+absolute_variation))
    return laptime

track_distance = 5403
elapsed_time = 0
lap_limit = 5

car1_baselp = toMillisecond(80)
car1_lp = randomlaptime(car1_baselp, 0.1)
car1_dist = 0
car1_lap = 0
car1_status = "run"

car2_baselp = toMillisecond(80)
car2_lp = randomlaptime(car2_baselp, 0.1)
car2_dist = 0
car2_lap = 0
car2_status = "run"

finisher = []

race_on = True

while race_on:
    elapsed_time += 1
    car1_dist += speed(car1_lp, track_distance)
    car2_dist += speed(car2_lp, track_distance)
    
    if car1_dist >= track_distance:
        car1_dist = 0
        car1_lap+=1
        print(f"Car 1 has completed {car1_lap} laps in {car1_lp/1000} s")
        car1_lp = randomlaptime(car1_baselp, 0.1)

    if car2_dist >= track_distance:
        car2_dist = 0
        car2_lap+=1
        print(f"Car 2 has completed {car2_lap} laps in {car2_lp/1000} s")
        car2_lp = randomlaptime(car2_baselp, 0.1)
   
    if car1_lap >= lap_limit:
        finisher.append("Car 1")
    if car2_lap >= lap_limit:
        finisher.append("Car 2")

    if len(finisher) >= 2:
        race_on = False
    

print(f"{finisher[0]} has won the race")
