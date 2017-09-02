#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Aug 26 08:23:40 2017

@author: Juan Antonio Barragán Noguera
@email : jabarragann@unal.edu.co

"""

from math import factorial as factorial
import math

def besselPolynoms(x):    
    ans=0
    
    for k in range (1,21):
        ans+=((x/2)**k/factorial(k))**2
        
    
    return 1+ans



def KaiserBesselWindow(ds,dp,delta_f,fs):
    
    delta = min(ds,dp)
    as1= -20*math.log10(delta)
    
    if as1>50:
        alfa=0.1102*(as1-8.7)
         
    elif as1<21:
        alfa=0 
    else:
        alfa=0.5842(as1-21)**0.4+0.07886*(as1-21)
    
    if as1<21:
        D=0.922
    else:
        D=(as1-7.95)/14.36
        
    N=fs*D/delta_f+1
    N=math.ceil(N)
    

KaiserBesselWindow(0.1,0.08,100,8000)

'''
for i in range(10):
    print(besselPolynoms(i))
'''   
    
    