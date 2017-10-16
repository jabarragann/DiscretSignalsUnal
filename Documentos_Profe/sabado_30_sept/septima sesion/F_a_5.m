clear all;
for i=1:100000
refruido(i) = (1*cos(2*pi*(i-1)*82.68/11025)); %cos(312)
end;

[dplusn,F] = audioread('ecg.wav');
plot (dplusn);

o_s=zeros(4000,1);
o_e=zeros(4000,1);
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
o_e(1) = dplusn(bc); 
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

for i=1:3998
    o_s(4000-i)=o_s(3999-i);
    o_e(4000-i)=o_e(3999-i);
end;
o_s(1)=output;
delay(1) = refruido(bc); 
plot (o_s);
hold on;
grid on;
plot (o_e,'r');
grid on;
ylim([-1 1]);
j=j+1;
pause(0.0000000001);
end;

