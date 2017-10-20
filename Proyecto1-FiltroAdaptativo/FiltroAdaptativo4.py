# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 23:24:05 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""


import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np
import Plotter as mp
import padasip as pa

FS=8000
n1 = 31
n2=n1+20
hCoeff = signal.firwin(n1,nyq=4000,cutoff = 100, window = "hamming")
inputSize=16000

#Frequency and phase response
omega, mag = signal.freqz(hCoeff)
freq=FS*omega/(2*np.pi)

#generate Input
t=np.linspace(0,0.1,inputSize)
x=5*np.sin(2*np.pi*300*t)
for i in range (len(x)):
    if x[i]>0: 
        x[i]=5
    else:
        x[i]=-5
        
noise=np.random.normal(0,1,inputSize)*0.1
x=x+noise
x=x/max(x)

#generate Output
d=signal.lfilter(hCoeff,[1.0],x)

#inputMatrix
inputMatrix=pa.input_from_history(x, n2)
#inputMatrix=np.zeros((inputSize,n1+20))
#for i in range(n1):
 #   inputMatrix[:,i]=x

# identification
f = pa.filters.FilterNLMS(mu=0.8, n=n2)
y, e, w = f.run(d, inputMatrix)

omega, mag2 = signal.freqz(w[-1],omega)



#Plot
fig,ax=plt.subplots(4)
mp.myPlotter(ax[0],freq,abs(mag))
mp.myPlotter(ax[0],freq,abs(mag2),param_dict={'color':'red'})

mp.myPlotter(ax[1],t,x)
mp.myPlotter(ax[2],t[:],d)
mp.myPlotter(ax[2],t[:],y,param_dict={'color':'red'})

mp.myPlotter(ax[3],np.arange(0,n1),hCoeff,stem=True)
mp.myPlotter(ax[3],np.arange(0,n1+20),w[-1],param_dict={'color':'red'},stem=True)

mp.myPlotterShow(fig)

#print("The original coefficients where: {}".format(hCoeff[:]))
#print("And the resulting coefficients are: {}".format(w[-1]))