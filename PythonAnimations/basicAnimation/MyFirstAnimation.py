# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 21:59:19 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.grid()
xdata, ydata = [], []
#ln, = plt.plot([], [], 'ro', animated=True)
ln, = plt.plot([], [], animated=True)

xdata=np.linspace(0,6,400)
ydata=np.sin(2*np.pi*xdata)

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

ani = FuncAnimation(fig, update, frames=1000,init_func=init,  interval=20,blit=True)

#plt.show()

