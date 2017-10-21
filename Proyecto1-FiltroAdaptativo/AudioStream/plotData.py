# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:37:15 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""

import matplotlib.pyplot as plt



data=open('desiredOutput1.txt','r')

arr=[]
for i in data:
    arr.append(float(i))
    
    
plt.plot(arr)