clear all;
for i=1:100000
refruido(i) = (1*cos(2*pi*(i-1)*82.68/11025)); %cos(312)
end;

[dplusn,F] = audioread('ecg.wav');
plot (dplusn);

o_s=zeros(100000,1);
o_e=zeros(100000,1);
Fs= 8000; %Fijar frecuencia de muestreo

beta =  1E-5; %Rata de convergencia del filtro
N  = 100; % #  de coeficientes 
NS = 128; % # de Puntos de salida
out_type = 1; % Selección de la salida

w=zeros(100,1);
delay=zeros(100,1);

j=1;
bc =1; % Inicializar conteo
while j<100000

hold off;

delay(1) = refruido(bc); 

yn = 0; 
for i = 1:N % Calculo del filtro
    yn = yn + w(i) * delay(i); 
end;
E = dplusn(bc) - yn; % Calculo del Error
for i = N:-1:1  % Actualizar coeficientes del filtro
    w(i) = w(i) + beta*E*delay(i); 
     if i ~=1        
        delay(i) = delay(i-1); % Actualizar buffer
     end;
end;
bc = bc+1;

%for i=1:3998
%    o_s(10000-i)=o_s(3999-i);
%    o_e(10000-i)=o_e(3999-i);
%end;
o_s(bc)=E;
o_e(bc) = dplusn(bc); 
if bc<8000
    t1=1;
    t2=8000;
else
    t1=bc-7999;
    t2=bc;
end;
plot (o_s(t1:t2));
hold on;
grid on;
plot (o_e(t1:t2),'r');
grid on;
ylim([-1 1]);
j=j+1;
%pause(0.000001);
end;

