 ## Melody Simon-says prototype ##
import os
import random
from pydub import AudioSegment
from pydub.playback import play

on = True
melodySize = 2
melody = []
sounds = ['C4.wav', 'G4.wav'] 
seed = 0
while on:
    random.seed(seed)

    melody = random.sample(range(0,melodySize), melodySize)
    relation = melody[1] - melody[0]

    for i in range(melodySize):
        sound = AudioSegment.from_wav(sounds[melody[i]])
        play(sound)

    ans = input('Pitch movement (^/v/>): ')


    if relation < 0:
        sol = 'v'
    elif relation == 0:
        sol = '>'
    elif relation > 0:
        sol = '^'
    
    if ans == sol:
        print('Correct!')
    else:
        print('Incorrect, the correct answer is : ' + sol)


    again = input('Another round? (Y/N)')
    if again == 'N':
        on = False
    seed += 1
