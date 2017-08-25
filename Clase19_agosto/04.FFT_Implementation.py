#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Aug 24 21:36:12 2017

@author: Juan Antonio Barragán Noguera
@email : jabarragann@unal.edu.co

"""
import Plotter
Plotter.IPythonReset()

import Plotter
import numpy as np 
import matplotlib.pyplot as plt 
import Plotter

def myFFT(x):
    
    x=np.array(x)
    N=len(x)
    W_N=np.exp(-2j*np.pi/N)
    
    if(N>2):
        even=np.array([ x[2*i] for i in range( int(N/2) ) ])
        odd=np.array( [ x[2*i+1] for i in range( int(N/2) ) ])
        
        even=myFFT(even)
        
        odd=myFFT(odd)
        
        ans=np.zeros(N,dtype=complex)
        
        for i in range(N):
            ans[i]=even[i%int(N/2)]+odd[i%int(N/2)]*W_N**i
        
        return ans
    else:
        return np.array([x[0]+x[1]*W_N**0,x[0]+x[1]*W_N**1],dtype=complex)


n=np.arange(64)
x=np.sin(2*np.pi*n*8/64)
X_mag=abs(np.fft.fft(x))
X2_mag=abs(myFFT(x))

fig,ax = plt.subplots(3)

Plotter.myPlotter(ax[0],n,x,{'Color':'green'},stem=True)
Plotter.myPlotter(ax[1],n,X_mag,{'Color':'blue'},stem=True)
Plotter.myPlotter(ax[1],n,X2_mag,{'Color':'red'},stem=True)
Plotter.myPlotter(ax[2],n,X2_mag,{'Color':'blue'},stem=True)

Plotter.myPlotterShow(fig)

