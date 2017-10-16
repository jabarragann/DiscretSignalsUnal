//AdaptIDIIR.c Adaptive FIR for system ID of fixed IIR using C67x tools

#include "bp2000.cof"   	         //BP @ 2kHz fixed IIR coeff
#include "noise_gen.h"		         //support file noise sequence
#define beta 1E-11                     //rate of convergence 
#define WLENGTH 200                    //# of coeff for adaptive FIR 
float w[WLENGTH+1];                    //buffer coeff for adaptive FIR
int dly_adapt[WLENGTH+1];              //buffer samples of adaptive FIR
int dly_fix[stages][2] = {0};          //delay samples of fixed IIR
int a[stages][3], b[stages][2];        //coefficients of fixed IIR                      
short out_type = 1;  	               //slider adaptive FIR/fixed IIR
int fb;				         //feedback variable for noise 
shift_reg sreg;			         //shift register for noise 

int prand(void) 			         //pseudo-random sequence {-1,1}
{
  int prnseq;
  if(sreg.bt.b0)
	prnseq = -4000; 		         //scaled negative noise level
  else
	prnseq= 4000;		         //scaled positive noise level 
  fb =(sreg.bt.b0)^(sreg.bt.b1);       //XOR bits 0,1
  fb^=(sreg.bt.b11)^(sreg.bt.b13);     //with bits 11,13 ->fb
  sreg.regval<<=1;
  sreg.bt.b0=fb;			         //close feedback path
  return prnseq;				   //return noise sequence 
}

interrupt void c_int11()               //ISR
{                         
 int i, un, input, yn;
 int iir_out=0;			         //init output of fixed IIR
 int adaptfir_out=0;		         //init output of adaptive FIR
 float E;				         //error signal	

 dly_fix[0][0] = prand();  	         //input noise to fixed IIR	
 dly_adapt[0] = dly_fix[0][0];         //same input to adaptive FIR
 input = prand();		           	   //noise as input to fixed IIR	
 
 for (i = 0; i < stages; i++)          //repeat for each stage
  {
  un=input-((b[i][0]*dly_fix[i][0])>>15)-((b[i][1]*dly_fix[i][1])>>15);
  
  yn=((a[i][0]*un)>>15)+((a[i][1]*dly_fix[i][0])>>15)
     +((a[i][2]*dly_fix[i][1])>>15);
  
  dly_fix[i][1] = dly_fix[i][0];       //update delays of fixed IIR
  dly_fix[i][0] = un;                  //update delays of fixed IIR
  input = yn;  		        	   //in next stage=out previous 
  }
 
 iir_out = yn;                         //output of fixed IIR
 
 for (i = 0; i < WLENGTH; i++)
   adaptfir_out +=(w[i]*dly_adapt[i]); //output of adaptive FIR
 
 E = iir_out - adaptfir_out;  	   //error as difference of outputs          
 
 for (i = WLENGTH; i > 0; i--)         
  {
   w[i] = w[i]+(beta*E*dly_adapt[i]);  //update weights of adaptive FIR  
   dly_adapt[i] = dly_adapt[i-1];      //update samples of adaptive FIR
  } 
 
 if (out_type == 1)			   //slider adaptive FIR/fixed IIR 
   output_sample(adaptfir_out);        //output of adaptive FIR
 else if (out_type == 2)
   output_sample(iir_out);             //output of fixed IIR 
 return;					   //return to main
}

void main()
{
 int i=0;
 for (i = 0; i < WLENGTH; i++)
  {
   w[i] = 0.0;       			   //init coeff of adaptive FIR
   dly_adapt[i] = 0.0;                 //init samples of adaptive FIR
  }
 sreg.regval=0xFFFF;	               //initial seed value
 fb = 1;			               //initial feedback value
 comm_intr();                          //init DSK, codec, McBSP
 while (1);                            //infinite loop
}

