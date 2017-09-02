#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Aug 25 00:01:05 2017

@author: Juan Antonio Barragán Noguera
@email : jabarragann@unal.edu.co

"""

import Plotter
Plotter.IPythonReset()

import Plotter
import numpy as np 
import matplotlib.pyplot as plt 
from timeit import default_timer as timer

def myFFT(x):
    
    x=np.array(x)
    N=len(x)
    W_N=np.exp(-2j*np.pi/N)
    
    if(N>2):
        even=np.zeros(int(N/2))
        odd=np.zeros(int(N/2))
        
        for i in range( int(N/2) ):    
            even[i]= x[2*i]
            odd[i] = x[2*i+1] 
        
        even=myFFT(even)
        
        odd=myFFT(odd)
        
        ans=np.zeros(N,dtype=complex)
        
        for i in range(N):
            ans[i]=even[i%int(N/2)]+odd[i%int(N/2)]*W_N**i
        
        return ans
    else:
        return np.array([x[0]+x[1]*W_N**0,x[0]+x[1]*W_N**1],dtype=complex)

def myDFT(x) :
    
    x=np.array(x)
    
    N=x.shape[0]
    X=np.zeros(N,dtype=np.complex_)

    for k in range(N):
        for n in range(N):
            
            X[k]+=x[n]*np.exp(-2j*np.pi*k*n/N)
            
    return X


#test Signal
n=np.arange(1024)
x=np.sin(2*np.pi*2*n/64)

#generate Figure
stem_var=False
fig,ax = plt.subplots(4)

#DFT calculations

startTime=timer()
X1=abs(myDFT(x))
print("DFT slow---------- %s seconds ----" % (timer()-startTime))
Plotter.myPlotter(ax[1],n,X1,{'Color':'blue'},stem=stem_var)


startTime=timer()
X2=abs(myFFT(x))
print("DFT myFFT--------- %s seconds ----" % (timer()-startTime))
Plotter.myPlotter(ax[2],n,X2,{'Color':'green'},stem=stem_var)

startTime=timer()
X3=abs(np.fft.fft(x))
print("DFT python FFT---- %s seconds ----" % (timer()-startTime))
Plotter.myPlotter(ax[3],n,X3,{'Color':'orange'},stem=stem_var)

print("\n \n")

Plotter.myPlotter(ax[0],n,x,{'Color':'red'},stem=stem_var)

Plotter.myPlotterShow(fig)
