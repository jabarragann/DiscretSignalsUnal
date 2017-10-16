#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Sep 14 22:51:07 2017

@author: Juan Antonio Barragán Noguera
@email : jabarragann@unal.edu.co

"""

import control as ct 
import numpy as np 
import matplotlib.pyplot as plt
import Plotter as mp

def setGraphLabels(ax,title):
    ax.set_title(title)
    ax.set_xlabel("Freq (Hz)")
    ax.set_ylabel("Mag")
    
#System1 Variables
r1=20e3
r2=100
r3=10e3
c1=0.1e-6

#Define the transfer function
num= np.array([r1*r2*c1,0])
den= np.array([r1*r2*r3*c1**2,2*r2*r3*c1,r2+r3])
sys1 = ct.tf(num, den)

FS=8000
sys1_d=ct.sample_system(sys1, 1/FS, method='tustin')

#print tf
print("#"*55)
print("#"*10+" System 1")
print("#"*55)
print(sys1)
print(sys1_d)
print("#"*55)
print("#"*55)

#generate Bode
omega=np.linspace(0.1,4000*2*np.pi,6000,endpoint=True)
mag, phase, omega = ct.bode(sys1,omega,dB=False,Plot=False)
freq=omega/(2*np.pi)

#System2 Variables
r1=5.1e3
r2=5.1e3
r3=1000
r4=1080
c1=0.1e-6

#middle Variables
parallel=r1/2
a=-parallel/r1+1/r3-1/r1-1/r4
b=1/r3+1/r1
c=parallel/(r2*r4)+parallel*b/r2+1/r4

num2= np.array([r2*r4*c1**2,-a*r2*r4*c1,parallel])
den2= np.array([parallel*c1*r4,c*r2*r4*c1,b*parallel])
sys2 = ct.tf(num2, den2)

#generate Bode
omega=np.linspace(0.1,4000*2*np.pi,6000,endpoint=True)
mag2, phase2, omega = ct.bode(sys2,omega,dB=False,Plot=False)
freq=omega/(2*np.pi)


#print tf
print("\n")
print("#"*55)
print("#"*10+" System 2")
print("#"*55)
print(sys2)
#print(sys1_d)
print("#"*55)
print("#"*55)


#Plot transfer functions frequency response
fig,ax=plt.subplots(2)
mp.myPlotter(ax[0],freq,abs(mag))
mp.myPlotter(ax[1],freq,abs(mag2))


setGraphLabels(ax[0],"System 1")
setGraphLabels(ax[1],"System 2")
plt.tight_layout()

mp.myPlotterShow(fig)
