#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Sep  9 09:22:23 2017

@author: Juan Antonio Barragán Noguera
@email : jabarragann@unal.edu.co

"""

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *

#Continous transfer funcion

ft = signal.TransferFunction([2*np.pi*1000], [1, 2*np.pi*1000])
w, mag, phase = signal.bode(ft)


ft_d = tf([2*np.pi*1000,2*np.pi*1000], [2*np.pi*1000+16000, 2*np.pi*1000-16000],1/8000)
w_d, mag_d, phase_d = bode(ft_d)


plt.figure()
plt.grid()
plt.semilogx(w, mag)    # Bode magnitude plot
plt.semilogx(w_d, mag_d)    # Bode magnitude plot

#plt.figure()
#plt.semilogx(w, phase)  # Bode phase plot
#plt.grid()





plt.show()