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

#Define the transfer function
num= np.array([2000*np.pi])
den= np.array([1,2000*np.pi])
sys1 = ct.tf(num, den)


#print tf
print(sys1)

#generate Bode
mag, phase, omega = ct.bode(sys1,dB=True)


fig,axes=plt.subplots(2)


mp.myPlotterBode(axes[0],axes[1],omega,mag,phase)
mp.myPlotterShow(fig)

