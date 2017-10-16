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
import Plotter as mp

#Sound stream Variables
q=queue.Queue() 
duration = 5.5  # seconds
FS=8000

#Animation Variables
plt.ion()
fig, ax = plt.subplots(1)
ax.grid()
xdata=np.arange(4000)
ydata=np.zeros(4000)
ln, = ax.plot(xdata, ydata, animated=True)


def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
        
    q.put(indata[:])
    outdata[:] = indata

def init():
    ax.set_xlim(1200, 1400)
    ax.set_ylim([-0.2,0.2])
    return ln,

def update(frame):    
    if not q.empty():
        dataBlock=q.get_nowait()
        index=0
        for data1 in dataBlock:
            ydata[frame*100+index]=data1
            index+=1
            
    ln.set_data(xdata, ydata)
    return ln,

try:
    stream=sd.Stream(samplerate=FS,channels=1,blocksize=100, callback=callback)
    ani = FuncAnimation(fig, update, frames=40,init_func=init,  interval=10,blit=True)
    mp.myPlotterStreamShow(fig,stream)
    
    plt.show()
    stream.start()
    
except Exception as e:
    stream.stop()
    print("Error")
