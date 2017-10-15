clear all;
for i=1:100000
refruido(i) = (1*cos(2*pi*(i-1)*60/8000)); %cos(312)
end;
m=4000;
[dplusn,F] = audioread('ecg.wav');
plot (dplusn);

o_s=zeros(m,1);
o_e=zeros(m,1);
Fs= 8000; %Fijar frecuencia de muestreo

beta =  1E-4; %Rata de convergencia del filtro
N  = 30; % #  de coeficientes 
NS = 128; % # de Puntos de salida
out_type = 1; % Selección de la salida

w=zeros(30,1);
delay=zeros(30,1);

j=1;
bc =1; % Inicializar conteo
while j<100000



delay(1) = refruido(j); 
o_e(1) = dplusn(j); 
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

if out_type == 1 % Seleccionar tipo de salida
    output = E; % Salida filtrada
    elseif out_type == 2
        output=dplusn(bc); % Mostrar la señal de entrada con ruido
end;

for i=1:m-2
    o_s(m-i)=o_s(m-1-i);
    o_e(m-i)=o_e(m-1-i);
end;


o_s(1)=output; 
o_sfft=fft(o_s);
o_sfft=abs(o_sfft);

delay(1) = refruido(bc); 
subplot (3,1,1),plot (o_s(1:m));

grid on;

subplot (3,1,2),plot (o_e(1:m));
grid on;
subplot (3,1,3),plot (o_sfft(1:100));
grid on;
j=j+1;
%pause(0.01);
end;

