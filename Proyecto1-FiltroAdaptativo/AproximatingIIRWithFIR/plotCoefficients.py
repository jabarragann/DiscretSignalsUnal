# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 01:58:11 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""

import matplotlib.pyplot as plt
import scipy.signal as signal
import Plotter as mp
import numpy as np

#Global variables
FS=8000
TS=1/FS
nyq=FS*0.5
numberOfTaps=47

hcoeff=signal.firwin(numberOfTaps,[300, 600], pass_zero=False, nyq=nyq)

hestimate=[]
coeffFile=open('WEIGHTS.TXT','r')

count=0
for i in coeffFile:
    if count>0:
        temp=i.split(',')
        hestimate.append(float(temp[1][:-2]))
    count+=1
    
fig,axes=plt.subplots(2)

mp.myPlotter(axes[0],np.arange(0,numberOfTaps),hestimate,stem=True)
#mp.myPlotter(axes[0],np.arange(0,25),h,stem=True)


w, h = signal.freqz(hestimate,[1])
mp.myPlotter(axes[1],w,abs(h))

#Butterworth
numButterworth, denButterworth = signal.butter(1, [300/nyq,600/nyq], btype='bandstop',output='ba')

#Project Transfer Function
num=[0.04961,6.661e-16,-0.04961]
den=[1,-1.274,0.9008]

wButterworth, hButterworth = signal.freqz(num,den)
mp.myPlotter(axes[1],wButterworth,abs(hButterworth),{'color':'red'})

mp.myPlotterShow(fig)