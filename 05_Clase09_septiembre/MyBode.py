#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Sep 16 17:01:35 2017

@author: Juan Antonio Barragán Noguera
@email : jabarragann@unal.edu.co

"""


import control as ct 
import numpy as np 
import matplotlib.pyplot as plt
import Plotter as mp 
 

 
def myBode(sys,omega,fs,dB=True):
    print(sys)     
    num,den = ct.tfdata(sys)
    num=np.array(num)
    den=np.array(den)
    num=num[0][0,:]
    den=den[0][0,:]
    print(num)
    print(den)
    
    mag=np.zeros(len(omega))
    phase=np.zeros(len(omega))
    
    numLen=len(num)
    denLen=len(den)
    
    totalNum=0
    totalDen=0
    counter=0
    
    for w in omega:
        for i in range(numLen):
            totalNum=totalNum+num[i]*(np.exp(1j*w))**(numLen-i-1)
        
        for i in range(denLen):
            totalDen=totalDen+den[i]*(np.exp(1j*w))**(denLen-i-1)
        
        if dB:
            mag[counter]=20*np.log(abs(totalNum/totalDen))
        else:
            mag[counter]=abs(totalNum/totalDen)
        
        phase[counter]=np.angle(totalNum/totalDen,deg=True)
        
        counter=counter+1
        totalNum=0
        totalDen=0
        
    return mag,phase
 
    

#Define the transfer function
num= np.array([2000*np.pi])
den= np.array([1,2000*np.pi])
sys1 = ct.tf(num, den)

#Continous System Info
print(sys1)
num,den=ct.tfdata(sys1)
print(num)
print(den)

#Convert to discrete
fs=8000
sys2=ct.sample_system(sys1, 1/fs, method='tustin')

#Discrete System Info
print(sys2)
num2,den2=ct.tfdata(sys2)
print(num2)
print(den2)

#Discrete Bode
omega_disc=np.linspace(0.01,np.pi*3/4,6000)
magD,phaseD=myBode(sys2,omega_disc,fs)

#Continous Bode
magC, phaseC,omega_conti = ct.bode(sys1,omega_disc*fs,dB=True,deg=True,Plot=False)


#Plotting
fig,axes=plt.subplots(2)
axes[0],axes[1]=mp.myPlotterBodeLabels(axes[0],axes[1])

mp.myPlotterBode(axes[0],axes[1],omega_disc*fs/(2*np.pi),magD,phaseD,param_dict={'color':'red'})
mp.myPlotterBode(axes[0],axes[1],omega_conti/(2*np.pi),magC,phaseC)

#plot 3dB line and 60 deg line
mp.myPlotterBode(axes[0],axes[1],[omega_disc[0]*fs/(2*np.pi),omega_disc[-1]*fs/(2*np.pi)],[-3,-3],[-60,-60],param_dict={'color':'black'})


mp.myPlotterShow(fig)

