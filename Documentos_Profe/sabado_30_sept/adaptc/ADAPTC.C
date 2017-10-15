//ADAPTC.C - ADAPTATION USING LMS WITHOUT THE TI COMPILER
#include <stdio.h>
#include <math.h>
#define beta 0.01                      //convergence rate
#define N  21                          //order of filter 
#define NS  40                         //number of samples
#define Fs  8000                       //sampling frequency
#define pi  3.1415926                     
#define DESIRED 2*cos(2*pi*T*1000/Fs)  //desired signal
#define NOISE sin(2*pi*T*1000/Fs)      //noise signal

main()
{
 long I, T;
 double D, Y, E; 
 double W[N+1] = {0.0};
 double X[N+1] = {0.0};
 FILE *desired, *Y_out, *error;
 desired = fopen ("DESIRED", "w++"); //file for desired samples
 Y_out = fopen ("Y_OUT", "w++");     //file for output samples
 error = fopen ("ERROR", "w++");     //file for error samples
 for (T = 0; T < NS; T++)            //start adaptive algorithm
  {    
   X[0] = NOISE;                     //new noise sample
   D = DESIRED;                      //desired signal
   Y = 0;                            //filter'output set to zero
   for (I = 0; I <= N; I++)
    Y += (W[I] * X[I]);              //calculate filter output
   E = D - Y;                        //calculate error signal
   for (I = N; I >= 0; I--)         
    {
     W[I] = W[I] + (beta*E*X[I]);    //update filter coefficients
     if (I != 0)                     
     X[I] = X[I-1];                  //update data sample 
    }   
  fprintf (desired, "\n%10g    %10f", (float) T/Fs, D); 
  fprintf (Y_out, "\n%10g    %10f", (float) T/Fs, Y);
  fprintf (error, "\n%10g    %10f", (float) T/Fs, E);
  }   
  fclose (desired);
  fclose (Y_out);
  fclose (error);
}


