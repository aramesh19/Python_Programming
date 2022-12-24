#Healthy Programmer
#9am-5pm
# Water - water.mp3 (3.5 liters) - drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 mins - EyeDone - log - Every 30 min
# Physical activity - physical.mp3 - ExDone - log - every 45 min

from pygame import mixer
from datetime import datetime
from time import time


def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open('mylogs.txt','a') as f:
        f.write(f'{msg} {datetime.now()}\n')

if __name__ == '__main__':
    #musiconloop('water.mp3','stop')
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40*60
    physecs = 30*60
    eysecs = 45*60

    while True:
        if time() - init_water > watersecs:
            print('water drinking time. Enter "Drank" to stop the alarm.')
            musiconloop('water.mp3','drank')
            init_water = time()
            log_now('Drank water at')

        if time() - init_eyes > eysecs:
            print('Eye exercise time, Enter "doneeyes" to stop alarm')
            musiconloop('eyes.mp3','doneeyes')
            init_eyes = time()
            log_now('Eyes relaxed at')

        if time() - init_exercise > physecs:
            print('Physical activity time, enter "physical" to stop alarm')
            musiconloop('physical.mp3', 'physical')
            init_exercise = time()
            log_now('Physical activity done at')
