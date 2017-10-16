for i=1:10000
deseada(i) = round(100*sin(2*pi*(i-1)*500/8000)); %sin(1500)
addruido(i) = round(100*sin(2*pi*(i-1)*100/8000)); %sin(312)
refruido(i) = round(100*cos(2*pi*(i-1)*98/8000)); %cos(312)
end
dplusn = addruido + deseada; %sin(312)+sin(1500)
plot (dplusn);

o_s=zeros(128,1);

Fs= 8000; %Fijar frecuencia de muestreo

beta =  1E-8; %Rata de convergencia del filtro
N  = 30; % #  de coeficientes 
NS = 128; % # de Puntos de salida
out_type = 1; % Selección de la salida

for T = 1: 30
    w(T) = 0; %Inicializar coeficientes
    delay(T) = 0; %Inicializar buffer de trabajo
end;

j=1;
bc =1; % Inicializar conteo
while j<10000



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
bc=bc+1; 

if out_type == 1 % Seleccionar tipo de salida
    output = E*10; % Salida filtrada
    elseif out_type == 2
        output=dplusn(bc); % Mostrar la señal de entrada con ruido
end;

for i=1:126
    o_s(128-i)=o_s(127-i);
end;
o_s(1)=output; 
o_sfft=fft(o_s);
o_sfft=abs(o_sfft);

delay(1) = refruido(bc); 
subplot (2,1,1),plot (o_s),grid;
subplot (2,1,2),plot (o_sfft),grid;
j=j+1;
pause(0.01);
end;