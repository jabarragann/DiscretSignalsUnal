#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Sep 16 14:22:16 2017

@author: Juan Antonio Barragán Noguera
@email : jabarragann@unal.edu.co

"""



import control as ct 
import numpy as np 
import matplotlib.pyplot as plt
import Plotter as mp
import control.matlab as cm

#Define the transfer function
num= np.array([2000*np.pi])
den= np.array([1,2000*np.pi])
sys1 = ct.tf(num, den)

sys2=cm.c2d(sys1,1/8000,method='tustin')


#print tf
print(sys1)
print(sys2)

#generate Bode
mag, phase, omega = cm.bode(sys1,dB=True,Plot=False)
mag2, phase2, omega2 = cm.bode(sys2,dB=True,Plot=False)


fig,axes=plt.subplots(2)
fig2,axes2=plt.subplots(2)

mp.myPlotterBode(axes[0],axes[1],omega,mag,phase,param_dict={'color':'blue'})

mp.myPlotterBode(axes2[0],axes2[1],omega2,mag2,phase2,param_dict={'color':'red'})


axes[0].set_ylabel("Magnitude (DB)")
axes[1].set_ylabel("Phase (Rad)")


mp.myPlotterShow(fig)
mp.myPlotterShow(fig2)
