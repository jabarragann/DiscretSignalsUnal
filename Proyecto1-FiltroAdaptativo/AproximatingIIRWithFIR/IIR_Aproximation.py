# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 01:48:57 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""


import numpy as np
import random
import scipy.signal as signal

#Global variables
mu=0.1           #convergence rate
M=31			      #order of filter
I=270000			    #number of samples
FS=8000
TS=1/FS
nyq=FS*0.5

Input=np.zeros(I)
Desired=np.zeros(I)


#H[M] = [1.5,4.6, 1, 0.5, 0.25, 0.125, 0.03 ];	the main system
#H =np.array([ 0.03, 0.125, 0.25, 0.5, 1,4.6,1.5 ])		#we need inverse of main system to convolution
#H=np.array([ 0.00508471,  0.07441537,  0.2810572 ,  0.41008104,  0.2810572 ,0.07441537,  0.00508471])

#Butterworth Filter
#num, den = signal.butter(1, [500/nyq,900/nyq], btype='band',output='ba')
num, den = signal.butter(2, [500/nyq,900/nyq], btype='bandstop',output='ba')

#FIR filter
#num= signal.firwin(M,[500, 700], pass_zero=False, nyq=nyq)
#den=[1]

def initialize():
    for i in range(I):
        Input[i]= random.random()

    for i in range(I):
        for j in range(M):
            if(i-j >= 0):
               Desired[i] += Input[i - j] * H[j]
    
    return Desired

def initialize2():
    #desired output with IIR filter
    for i in range(I):
        Input[i]= random.random()
    
    Desired=signal.lfilter(num,den,Input)
    return Desired

def initialize3():
    #desired output with FIR filter
    for i in range(I):
        Input[i]=random.random()
        
    Desired=signal.lfilter(num,[1],Input)
    return Desired
    	
def main():
    
    Desired=initialize2()
    #Desired=initialize()
    
    T=0
    D=0
    Y=0
    E=0
    
    W=np.zeros(M)
    X=np.zeros(M)
    
    Y_out=open('Y_OUT.txt','w')
    errors=open('ERROR.txt','w')
    weights=open('WEIGHTS.txt','w')

    for T in range(0,I):
        
        for m in range(T,T-M,-1):
            if m>= 0:
                X[M + (m - T) - 1] = Input[m];	#X new input sample for 
									#LMS filter
            else:
                break;
        
        D = Desired[T];					#desired signal
        Y = 0;
          
        for i in range(0,M):
            Y+=(W[i] * X[i]);  #calculate filter output
            
        
        E = D - Y;					#calculate error signal

        for i in range (0,M,1):
            W[i] = W[i] + (mu * E * X[i]);		#update filter coefficients
            
        Y_out.write('\n{:05d},{:04.10f}'.format(int(T),Y))
        errors.write('\n{:05d},{:04.10f}'.format(int(T),E))    
			

    for i in range(0,M,1):
        weights.write("\n{:05d},{:04.10f}".format( i, W[i]))
    
    Y_out.close()
    errors.close()
    weights.close()

main()