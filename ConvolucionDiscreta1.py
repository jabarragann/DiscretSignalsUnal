# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 22:08:18 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""

import numpy as np 
import Plotter as mp
from scipy import signal 
import matplotlib.pyplot as plt


#offline implementation 
x=[0.5,2,0,0,0]
h=[1,1,1]
y=signal.lfilter(h,[1.0],x)

fig,axes=plt.subplots(3)
for ax in axes:
    ax.grid()
    ax.set_ylim((-0.5,3.5))
axes[0].stem(x)
axes[1].stem(h)
axes[2].stem(y)

plt.show()