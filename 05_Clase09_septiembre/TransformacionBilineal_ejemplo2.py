#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Sep 17 01:05:30 2017

@author: Juan Antonio Barragán Noguera
@email : jabarragann@unal.edu.co

"""

import control as ct 
import numpy as np 
import matplotlib.pyplot as plt
import Plotter as mp

#Define continous system
num= [2*np.pi*100, 0]
den= [1,2*np.pi*100,4*(np.pi**2)*(5000*2) ]
sys_c = ct.tf(num, den)

#Sample continous system
fs=20000
sys_d=ct.sample_system(sys_c, 1/fs, method='tustin')

#Print Continous and Discrete system
print(sys_d)
print(sys_c)


#generate Continous transfer function Bode
omega=np.linspace(10,40000,10000,endpoint=True)
magC, phaseC, omegaC = ct.bode(sys_c,omega,dB=True,Plot=False)

#plot
fig,axes=plt.subplots(2)
mp.myPlotterBodeLabels(axes[0],axes[1])
mp.myPlotterBode(axes[0],axes[1],omega,magC,phaseC,param_dict={'color':'red'})

#Generate Discrete transfer function Bode
magD, phaseD, omegaD = ct.bode(sys_d,omega,dB=True,Plot=False)

#plot
mp.myPlotterBodeLabels(axes[0],axes[1])
mp.myPlotterBode(axes[0],axes[1],omega,magD,phaseD,param_dict={'color':'green'})

mp.myPlotterShow(fig)
