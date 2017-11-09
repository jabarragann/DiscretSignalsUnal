# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:37:15 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""

import matplotlib.pyplot as plt



data=open('desiredOutputTemp.txt','r')

arr=[]
for i in data:
    if i.strip()!="":
        arr.append(float(i.strip()))
    
    
plt.plot(arr)