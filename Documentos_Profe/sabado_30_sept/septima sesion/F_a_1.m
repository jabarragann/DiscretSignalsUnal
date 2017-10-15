clear all;
beta =  0.1; %Rata de Convergencia
N = 21; % Orden del Filtro
NS = 80; % Numero de Muestras
Fs =  8000; % Frecuencia de Muestreo

W = zeros(N+1,1);
X = zeros(N+1,1);

for T = 0:NS-1
    X(1) = sin(2*pi*T*600/Fs); % Nueva muestra de ruido
    D = 2*cos(2*pi*T*1000/Fs); % Señal Desaeada
    Y = 0; %Inicio de la salida del filtro
    for I = 0:N
        Y = Y+ W(I+1) * X(I+1); % Calculo de la salida del filtro
    end;
    E = D - Y; %Calcular señal de error
    for I = N:-1:0
        W(I+1) = W(I+1) + beta*E*X(I+1); %Actualización de Coeficientes
        if I ~=0
            X(I+1) = X(I); %Actualizar vector de entrada
        end;
    end;
desa(T+1)=D;
salida(T+1)=Y;
error(T+1)=E;

end;
plot (desa);
hold on;
plot (salida,'r');
grid on;
