[dplusn,F] = audioread('ecg.wav');
t=2*pi*60/8000;
r=0.99;
d=dplusn(1:3*F);
subplot (2,1,1),plot (d),grid;
n=[1 -2*cos(t) 1];
d=[1 -2*r*cos(t) r*r];
y=filter (n,d,dplusn);
subplot (2,1,2),plot (y(1:3*F)),grid;