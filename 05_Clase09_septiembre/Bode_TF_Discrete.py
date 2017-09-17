#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Sep 15 00:15:39 2017

@author: Juan Antonio Barragán Noguera
@email : jabarragann@unal.edu.co

"""

#Discrete system frequency response and bode diagram

import control as ct 
import numpy as np 
import matplotlib.pyplot as plt
import Plotter as mp

#Define continous system-num and den must normal arrays not numpy arrays.
num= [1,1]
den= [10,-8]
sys1 = ct.tf(num, den,1)

#print tf
print(sys1)

#generate Bode
omega=np.linspace(0.1,np.pi*3/4,6000,endpoint=True)
mag, phase, omega = ct.bode(sys1,omega,dB=True,Plot=False)

#plot
fig1,axes=plt.subplots(2)
mp.myPlotterBodeLabels(axes[0],axes[1])
mp.myPlotterBode(axes[0],axes[1],omega,mag,phase)
mp.myPlotterShow(fig1)

#generate frequency response
omega=np.linspace(0.1,4*2*np.pi,6000,endpoint=True)
mag, phase, omega = ct.bode(sys1,omega,dB=False,Plot=False)

#plot
fig2,axes2=plt.subplots(2)
mp.myPlotterBodeLabels(axes2[0],axes2[1])
mp.myPlotter(axes2[0],omega,mag,param_dict={'color':'red'})
mp.myPlotter(axes2[1],omega,phase,param_dict={'color':'red'})
mp.myPlotterShow(fig2)
