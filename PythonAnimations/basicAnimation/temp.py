# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 22:04:11 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""

import sounddevice as sd
import queue
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


#Sound stream Variables
q=queue.Queue() 
duration = 5.5  # seconds
FS=8000

#Animation Variables

plt.ioff()
fig, ax = plt.subplots()
ax.grid()
xdata, ydata = [], []
#ln, = plt.plot([], [], 'ro', animated=True)
ln, = ax.plot([1,2], [1,2], animated=True)

xdata=np.linspace(0,6,400)
ydata=np.sin(2*np.pi*xdata)
duration = 5.5  # seconds
FS=8000

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
        
    outdata[:] = indata

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim([-1.5,1.5])
    return ln,

def update(frame):    
    #xdata.append(frame)
    #ydata.append(np.sin(frame))
    ydata=np.sin(2*np.pi*xdata+0.04*frame)
    
    ln.set_data(xdata, ydata)
    return ln,

stream=sd.Stream(samplerate=FS,channels=1,blocksize=100, callback=callback)
ani = FuncAnimation(fig, update, frames=1000,init_func=init,  interval=20,blit=True)

with stream:
    plt.show()
    print('#'*40)
    print("Press enter to finish the stream!")
    print('#'*40)
    input()
    print("Programme has finished")
    
    