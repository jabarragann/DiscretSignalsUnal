# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 10:41:14 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""

import matplotlib.pyplot as plt
import numpy as np


FS=8000
TS=1/FS

f=1500

x=np.arange(0,200)
y=np.sin(2*np.pi*f*TS*x)


plt.stem(x,y)


