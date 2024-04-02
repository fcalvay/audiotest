# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:27:45 2019

@author: Utilisateur
"""

import math
import struct
import pyaudio
import numpy as np
import sys
import matplotlib.pyplot as pplot
from random import * 

def play_tone(frequency, amplitude, duration, fs, stream):
    N = int(fs / frequency)
    T = int(frequency * duration)  # repeat for T cycles
    dt = 1.0 / fs
    # 1 cycle
    seconds = duration # Note duration of 3 seconds

# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False,dtype = "float32")

# Generate a 440 Hz sine wave
    note = amplitude*np.sin(frequency * t * 2 * np.pi)
    # todo: get the format from the stream; this assumes Float32
    #data = ''.join(struct.pack('d', samp) for samp in note)
    for n in range(T):
        stream.write(note)
def Graph(lst,lst2) : 
    x = lst2
    y = lst
    pplot.plot(x,y)
    pplot.show()    
        
lst = []
lst2 = []

fs = 48000 #Fréquence d'échantillonage 
p = pyaudio.PyAudio()
stream = p.open(
   format=pyaudio.paFloat32,
   channels=1,
   rate=fs,
   output=True)

#Program is starting here 
"""
while True:
    selection = input("U: Create User\nQ: Quit")
    if selection is "Q" or selection is "q":
        print("Quitting")
        sys.exit()
    if selection is "U" or selection is "u":
        print("User")
        amplitude = 0.01
        while amplitude < 0.1 : 
            f = randint(50,15000)
            play_tone(f,amplitude,0.75,fs,stream)
            amplitude = amplitude * 1.01
            lst.append(f)
            lst2.append(amplitude)
"""           
amplitude = 0.01
while True : 
    selection = input("U:hearing\nI: unable to hear\nQ: Quit")
    f = randint(20,20000) #fréquence aléatoire 
    play_tone(f,amplitude,0.01,fs,stream)
    amplitude = amplitude * 1.01
    if selection is "I" or selection is "i":
        print("unable to hear") #On augmente l'amplitude lorsque l'on entend pas la note 
        amplitude = amplitude *1.01
    if selection is "U" or selection is "u":
        print("hearing")
        lst.append(np.log(amplitude))
        lst2.append(np.log(f))
        amplitude = 0.01
    if selection is "Q" or selection is "q":
        print("Quitting")
        break
        
Graph(lst,lst2)
stream.close()
p.terminate()


    

 #play_tone(440, 0.1, 0.75, fs, stream)
        
        