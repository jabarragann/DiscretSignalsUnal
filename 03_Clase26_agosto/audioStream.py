# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 22:57:06 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""

import sounddevice as sd
import numpy as np

duration = 5.5  # seconds
FS=8000
TS=1/FS


def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
        
    
    testSignal=np.zeros((frames,1))
    t=0    
    for i in range(frames):
        testSignal[i]=0.5*np.sin(2*np.pi*1000*t*TS)
        '''
        if testSignal[i]>=0:
            testSignal[i]=0.5
        else:
            testSignal[i]=-0.5
        
        print(testSignal[i])
        '''
        
        t=t+1
    
    outdata[:] = testSignal

with sd.Stream(samplerate=FS,channels=1,blocksize=200, callback=callback):
    #sd.sleep(int(duration * 1000))
    print('#'*40)
    print("Press enter to finish the stream!")
    print('#'*40)
    input()
    print("Programme has finished")
    

