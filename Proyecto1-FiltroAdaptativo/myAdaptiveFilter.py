# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 23:16:22 2017

@author: Juan Antonio Barragán Noguera
@email: jabarragann@unal.edu.co

"""

import numpy as np
import random

#Global variables
mu=0.2          #convergence rate
M=7				   #order of filter
I=1000			   #number of samples

Input=np.zeros(I)
Desired=np.zeros(I)


#double H[M] = [1.5,4.6, 1, 0.5, 0.25, 0.125, 0.03 ];	the main system
H =np.array([ 0.03, 0.125, 0.25, 0.5, 1,4.6,1.5 ])		#we need inverse of main system to convolution


def initialize():
    for i in range(I):
        Input[i]= random.random()

    for i in range(I):
        for j in range(M):
            if(i-j >= 0):
               Desired[i] += Input[i - j] * H[j]
           
    	
def main():
    
    initialize()
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