# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 20:41:09 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""


from scipy import signal
import matplotlib.pyplot as plt
import Plotter as mp
import numpy as np
import random
import control as ct

FS=8000
TS=1/FS
nyq=FS*0.5
numtaps=25

num= signal.firwin(numtaps,[500, 700], pass_zero=False, nyq=nyq)
den=[1]

sys1 = ct.tf(num, [1],TS)
#print(sys1)

#Frequency Response
w, h = signal.freqz(num, [1])

#input signal
N=1000
f=600
n=np.arange(N)
x=np.sin(2*np.pi*f*n*TS)
noise = np.array([random.random() for i in range(1000)])
x=x+noise

#output signal
y=signal.lfilter(num,den,x)

 
fig,axes=plt.subplots(3)
axes[0].set_title("Butterworth Filter")
axes[1].set_title("Input signal + noise")
axes[2].set_title("Filtered signal")

mp.myPlotter(axes[0],(FS * 0.5 / np.pi)*w,abs(h))
mp.myPlotter(axes[1],n[:400]*TS,x[:400])
mp.myPlotter(axes[2],n[:400]*TS,y[:400])

mp.myPlotterShow(fig)

plt.tight_layout()