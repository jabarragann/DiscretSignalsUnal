#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Aug 19 04:07:21 2017

@author: Juan Antonio Barragán Noguera
@email : jabarragann@unal.edu.co

"""

import Plotter
Plotter.IPythonReset()

import Plotter
import numpy as np 
import matplotlib.pyplot as plt
from scipy import signal 




#filter exercise 1 

FS=8000
N=1000

#filter design
H= np.zeros(N)
w=(FS/N)*np.arange(0,N)

for i in range(25):
    H[i]=i/25
    H[N-1-i]=H[i]

for i in range(25,150):
    H[i]=1
    H[N-1-i]=H[i]

#test Signal
f0=320
n=np.arange(0,N)
x=5*np.sin(2*np.pi*f0*n/FS)
X_fft=np.fft.fft(x)

#filter1 signal 
Y_fft=X_fft*H
y=np.fft.ifft(Y_fft)

#filter2 signal
hCoeff=np.fft.ifft(H)
y2=signal.lfilter(hCoeff,[1.0],x)



fig,ax=plt.subplots(5)

stem_var=False
Plotter.myPlotter(ax[0],w,H,stem=stem_var)
Plotter.myPlotter(ax[1],n,x,stem=stem_var)
Plotter.myPlotter(ax[2],w,abs(X_fft),stem=stem_var)
Plotter.myPlotter(ax[3],n,y,stem=stem_var)
Plotter.myPlotter(ax[3],n,x,stem=stem_var,param_dict={'color':'red'})
Plotter.myPlotter(ax[4],n,y2,stem=stem_var)
Plotter.myPlotter(ax[4],n,x,stem=stem_var,param_dict={'color':'red'})


Plotter.myPlotterShow(fig)