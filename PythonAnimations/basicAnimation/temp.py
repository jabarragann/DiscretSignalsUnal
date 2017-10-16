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

#control
#file1 = open("index.txt","w")
#file2 = open("data.txt","w") 

#Sound stream Variables
q=queue.Queue() 
duration = 5.5  # seconds
FS=8000

#Animation Variables
plt.ion()
fig, ax = plt.subplots()
ax.grid()
xdata, ydata = [], []
#ln, = plt.plot([], [], 'ro', animated=True)
ln, = ax.plot([1,2], [1,2], animated=True)

xdata=np.arange(4000)
ydata=np.zeros(4000)

#ydata=np.sin(2*np.pi*xdata)
duration = 5.5  # seconds
FS=8000

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
        
    q.put(indata[:])
    outdata[:] = indata

def init():
    ax.set_xlim(1200, 1350)
    ax.set_ylim([-0.2,0.2])
    return ln,

def update(frame):    
    #xdata.append(frame)
    #ydata.append(np.sin(frame))
    #ydata=np.sin(2*np.pi*xdata+0.04*frame)
    if not q.empty():
        dataBlock=q.get_nowait()
        index=0
        for data1 in dataBlock:
            #file1.write(frame*100+index)
            #file2.write(data1)
            ydata[frame*100+index]=data1
            index+=1
            
    ln.set_data(xdata, ydata)
    return ln,

try:
    stream=sd.Stream(samplerate=FS,channels=1,blocksize=100, callback=callback)
    ani = FuncAnimation(fig, update, frames=40,init_func=init,  interval=10,blit=True)
    
    plt.show()
    stream.start()
except Exception as e:
    stream.stop()
    print("Stop excution")

#with stream:
 #   plt.show()
   