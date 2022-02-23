 ## Melody Simon-says prototype ##
import os
import random
from pydub import AudioSegment
from pydub.playback import play
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: "+str(rc))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected Disconnect")
    else:
        print("Expected Disconnect")

def on_message(client, userdata, message):
    print('Received message: "' + str(message.payload) + '" on topic "' +
        message.topic + '" with QoS ' + str(message.qos))

client = mqtt.Client()

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect_async("test.mosquitto.org")
client.loop_start()

on = True
melodySize = 4
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

    sol = ''
    for i in range(len(relation)):
        if relation[i] < 0:
            sol += 'v'
        elif relation[i] == 0:
            sol += '>'
        elif relation[i] > 0:
            sol += '^'

## Publish the melody and correct answer

client.publish('ece180d/test', melody, qos=1)
client.publish('ece180d/test', sol, qos=1)

## Here's how the keyboard input is processed

    for i in range(melodySize):
        sound = AudioSegment.from_wav(sounds[melody[i]])
        play(sound)

## Answer's made on client side instead of this:

#    ans = input('Pitch movement (^/v/>): ')
    
## How to store subscribed message?
#    ans = client.loop_start()
    if ans == sol:
        print('Correct!')
    else:
        print('Incorrect, the correct answer is : ' + sol)


    again = input('Another round? (Y/N)')
    if again == 'N':
        on = False
    seed += 1
