#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Aug 19 03:06:20 2017

@author: Juan Antonio Barragán Noguera
@email : jabarragann@unal.edu.co

"""



import matplotlib.pyplot as plt
import numpy as np 
import scipy as sc

FS=8000



#sine signal 
f0=250
N=2000
n=np.arange(0,N)
y=np.sin(2*np.pi*f0*n/FS)

plt.plot(n,y)
