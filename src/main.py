from car import *
from track import *
from race import *
from functions import *

 

#List of cars in the race
porsche = Car(92, toMillisecond(80))
aston = Car(95, toMillisecond(80))
ferrari = Car(51, toMillisecond(90))
cars = [porsche, aston, ferrari]

#Track
track = Track("Paul Ricard", 5842)

#Race
race = Race(lap_limit = 100)

def main():
    print('RaceStrategy 0.0')
    play_race(cars, track, race)

def play_race(cars, track, race):
    finishers = []
    #Main simulation loop :
    while len(finishers) < len(cars): 
        race.elapsed_time += 1

        #Going over each car : 
        for car in cars:
            if car not in finishers:
                car.distance += speed(car.laptime, track.distance)
                car.elapsed_time += 1
                if car.distance >= track.distance:
                    car.distance = 0
                    car.lapcount += 1
                    print(f"Car {car.number} has completed {car.lapcount} laps, last laptime : {car.laptime/1000} s")
                    car.laptime = randomlaptime(car.baselaptime, 0.1)
                if car.lapcount >= race.lap_limit:
                    finishers.append(car)

    #Resultats : 
    print("The Race is Finished ! ")
    print("Classification : ")
    for i in range(len(finishers)):
        print(f"{i+1}. {finishers[i].number} + {(finishers[i].elapsed_time - finishers[0].elapsed_time)/1000} s")

if __name__ == "__main__":
    main()
    