# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:04:57 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""

import sounddevice as sd
import numpy as np
import random


class TempInt():
    def __init__(self):
        self.count=0
        
duration = 2  # seconds
FS=8000
TS=1/FS
BLOCK_SIZE=200

counter1=TempInt()
testSignal=np.zeros((BLOCK_SIZE,1)) 

filename="desiredOutputTemp.txt"


#Clean Output file
desiredOutputFile=open(filename,'w')
desiredOutputFile.write("")
desiredOutputFile.close()

def callback(indata, outdata, blockSize, time, status):
    if status:
        print(status)

    for i in range(blockSize):
        #Sine Wave
        testSignal[i]=np.sin(2*np.pi*100*counter1.count*TS)
        #Square Wave
        #testSignal[i]= 1 if np.sin(2*np.pi*100*counter1.count*TS)>=0 else -1 
        #Random Wave
        #testSignal[i]=0.02*random.random()
        counter1.count=counter1.count+1
           
    outdata[:] = testSignal
    
    
    desiredOutputFile=open(filename,'a')
    for i in indata:
        desiredOutputFile.write('\n{:04.10f}'.format(float(i)))
    desiredOutputFile.close()
    

with sd.Stream(samplerate=FS,channels=1,blocksize=BLOCK_SIZE, callback=callback):
    sd.sleep(int(duration * 1000))
    
    '''
    print('#'*40)
    print("Press enter to finish the stream!")
    print('#'*40)
    input()
    print("Programme has finished")
    '''

