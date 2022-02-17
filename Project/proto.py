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
    for i in range(melodySize):
        melody.append(random.randint(0, len(sounds)-1))

    relation = [0]*(melodySize-1)
    for i in range(melodySize-1):
        relation[i] = melody[i+1] - melody[i]

    for i in range(melodySize):
        sound = AudioSegment.from_wav(sounds[melody[i]])
        play(sound)

    ans = input('Pitch movement (^/v/>): ')

    sol = ''
    for i in range(len(relation)):
        if relation[i] < 0:
            sol += 'v'
        elif relation[i] == 0:
            sol += '>'
        elif relation[i] > 0:
            sol += '^'

    if ans == sol:
        print('Correct!')
    else:
        print('Incorrect, the correct answer is : ' + sol)


    again = input('Another round? (Y/N)')
    if again == 'N':
        on = False
    seed += 1
