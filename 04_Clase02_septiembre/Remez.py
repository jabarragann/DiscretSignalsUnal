#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Sep  2 09:48:41 2017

@author: Juan Antonio Barragán Noguera
@email : jabarragann@unal.edu.co

"""

from scipy import signal
bpass = signal.remez(1000, [0, 200, 250, 450, 500, 650], [0, 1, 0],Hz=8000,maxiter=4000)
freq, response = signal.freqz(bpass)
ampl = np.abs(response)

import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(freq/(2*np.pi), ampl, 'b-')  # freq in Hz
plt.show()