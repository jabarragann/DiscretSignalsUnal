#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Sep  9 09:22:23 2017

@author: Juan Antonio Barragán Noguera
@email : jabarragann@unal.edu.co

"""

import control as ct 
import numpy as np 
import matplotlib.pyplot as plt
import Plotter as mp

#Define continous system
num= np.array([2000*np.pi])
den= np.array([1,2000*np.pi])
sys_c = ct.tf(num, den)

#Sample continous system
fs=8000
sys_d=ct.sample_system(sys_c, 1/fs, method='tustin')

#Print Continous and Discrete system
print(sys_d)
print(sys_c)


#generate Continous transfer function Bode
omega=np.linspace(100,10000,6000,endpoint=True)
mag, phase, omega = ct.bode(sys_c,omega,dB=True,Plot=False)

#plot
fig,axes=plt.subplots(2)
mp.myPlotterBodeLabels(axes[0],axes[1])
mp.myPlotterBode(axes[0],axes[1],omega,mag,phase,param_dict={'color':'red'})

#Generate Discrete transfer function Bode
mag, phase, omega = ct.bode(sys_d,omega,dB=True,Plot=False)

#plot
mp.myPlotterBodeLabels(axes[0],axes[1])
mp.myPlotterBode(axes[0],axes[1],omega,mag,phase,param_dict={'color':'green'})

mp.myPlotterShow(fig)
