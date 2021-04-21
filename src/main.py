from car import *
from track import *
from race import *
from functions import *

 

#List of cars in the race
porsche = Car(92, toMillisecond(80))
aston = Car(95, toMillisecond(80))
ferrari = Car(51, toMillisecond(90))
#Contains the cars in the race
cars = [porsche, aston, ferrari]

#Creating a start order

start_grid = cars

#Track
track = Track("Paul Ricard", 5842)

#Race
race = Race(lap_limit = 100)

def main():
    print('RaceStrategy 0.0')
    play_race(cars, track, race)

def play_race(cars, track, race):
    finishers = []
    printRace(start_grid, track, race)
    race_order = start_grid
    #Main simulation loop, simulates every ms :
    while len(finishers) < len(cars): 
        race.elapsed_time += 1

        #Going over each car to make it move forward: 
        for car in cars:
            if car not in finishers:
                car.distance += speed(car.laptime, track.distance)
                car.distance_total += speed(car.laptime, track.distance)
                car.elapsed_time += 1
                #Lap completion
                if car.distance >= track.distance:
                    car.distance = 0
                    car.lapcount += 1
                    print(f"Car {car.number} has completed {car.lapcount} laps, last laptime : {car.laptime/1000} s")
                    car.laptime = car.randomlaptime(car.baselaptime, 0.1)
                #Race completion by lap
                if car.lapcount >= race.lap_limit:
                    finishers.append(car)
                    car.status = "finish"
        
        #Finding the order 
        #Use a better sorting method than this
        for i in range(len(race_order)-1):
            m = i
            while race_order[i].distance_total < race_order[m+1].distance_total:
                m+=1
            race_order.insert(m+1, race_order[i])
            race_order.pop(i)

        if race.elapsed_time%600000 == 0:
            #print the order
            for i in range(len(race_order)):
                print(f"{i+1}. {race_order[i].number}")




    #Resultats : 
    print("The Race is Finished ! ")
    print("Classification : ")
    for i in range(len(finishers)):
        print(f"{i+1}. {finishers[i].number} + {(finishers[i].elapsed_time - finishers[0].elapsed_time)/1000} s")

if __name__ == "__main__":
    main()
    