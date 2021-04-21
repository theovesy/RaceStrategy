import random

def toMillisecond(time):
    return time*1000

def speed(laptimems, distance):
    return distance/laptimems

#prints info about the race
def printRace(start_grid, track, race):
    print(f"We are racing at {track.name} for {race.lap_limit}")
    print('Starting grid :')
    for i in range(len(start_grid)):
        print(f"{i+1} - #{start_grid[i].number}")
    print('==================')

