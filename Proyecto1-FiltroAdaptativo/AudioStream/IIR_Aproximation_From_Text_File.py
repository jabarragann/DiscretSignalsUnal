# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 08:05:17 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""
import matplotlib.pyplot as plt

desired=[]
inputFile=open('desiredOutputTemp.txt','r')

print(inputFile.read())
for i in inputFile:
    if i!="\n":
        desired.append(float(i))


plt.plot(desired)
plt.show()


