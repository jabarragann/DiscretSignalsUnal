#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Sep 15 00:15:39 2017

@author: Juan Antonio Barragán Noguera
@email : jabarragann@unal.edu.co

"""


import control as ct 
import numpy as np 
import matplotlib.pyplot as plt
import Plotter as mp

#Define the transfer function

num= np.array([2*np.pi*1000,2*np.pi*1000])
den= np.array([2*np.pi*1000+16000, 2*np.pi*1000-16000])
sys1 = ct.tf(num, den,1/8000)


#print tf
print(sys1)

#generate Bode
mag, phase, omega = ct.bode(sys1,dB=True)


fig,axes=plt.subplots(2)


mp.myPlotterBode(axes[0],axes[1],omega,mag,phase)
mp.myPlotterShow(fig)
