# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 22:57:06 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""

import sounddevice as sd

duration = 5.5  # seconds
FS=8000

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
        
    outdata[:] = indata

with sd.Stream(samplerate=FS,channels=1,blocksize=10, callback=callback):
    #sd.sleep(int(duration * 1000))
    print('#'*40)
    print("Press enter to finish the stream!")
    print('#'*40)
    input()
    print("Programme has finished")
    

