# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 22:17:15 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""


import sounddevice as sd
import queue
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import Plotter as mp
from LinkedList import myLinkedList

FS=8000
TS=1/FS
SIZE=1500
BLOCK_SIZE=1
myLinked=myLinkedList()
myLinked.zeros(SIZE)

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
    
    for i in range(100):
        q.put(indata[i])
        
    outdata[:] = indata

def init():
    ax.set_xlim(1000, 1400)
    ax.set_ylim([-0.2,0.2])
    return ln,

def update(frame):    
    if not q.empty():
        for i in range(8):
            myLinked.removeFromHead(1)
            myLinked.insertBeforeTail(q.get_nowait())
        
    ydata=myLinked.toArray()
    
    ln.set_data(xdata[1000:1400], ydata[1000:1400])
    return ln,
    

try:
    stream=sd.Stream(samplerate=FS,channels=1,blocksize=100, callback=callback)
    ani = FuncAnimation(fig, update, frames=40,init_func=init,  interval=150,blit=True)
    mp.myPlotterStreamShow(fig,stream)
    
    plt.show()
    stream.start()
    
except Exception as e:
    stream.stop()
    print("Error")
