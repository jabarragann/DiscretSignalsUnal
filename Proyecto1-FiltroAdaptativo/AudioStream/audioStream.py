# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:04:57 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""

import sounddevice as sd
import numpy as np
import random

duration = 5.5  # seconds
FS=8000
TS=1/FS

filename="desiredOutputTemp.txt"
filename="temp.txt"

#Clean Output file
desiredOutputFile=open(filename,'w')
desiredOutputFile.write("")
desiredOutputFile.close()

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
        
    
    testSignal=np.zeros((frames,1))
    t=0    
    for i in range(frames):
        testSignal[i]=np.sin(2*np.pi*60*t*TS)
        #testSignal[i]=0.02*random.random()
        t=t+1
           
    outdata[:] = testSignal
    
    
    desiredOutputFile=open(filename,'a')
    for i in indata:
        desiredOutputFile.write('\n{:04.10f}'.format(float(i)))
    desiredOutputFile.close()
    

with sd.Stream(samplerate=FS,channels=1,blocksize=200, callback=callback):
    #sd.sleep(int(duration * 1000))
    print('#'*40)
    print("Press enter to finish the stream!")
    print('#'*40)
    input()
    print("Programme has finished")
    

