% Datos experimentales
So = 400;
t = [6 12 14 16 19 22 24 28 31 35 37 38]; %tiempo(h)
DQO = [463.38 599.05 56.37 341.27 1470.75 256.48 171.68 320.93 314.14 236.13 297.18 225.95]; %DQO(mg/L)
% Grafico
figure('Name', 'Cinetica de primer orden')
subplot(1, 2, 1);
plot(t,DQO,'-o');
title("Datos experimentales");
xlabel("Tiempo(h)");
ylabel("DQO (mg/L)");
grid;
hold on;
subplot(1, 2, 2);
X = t;
Y = log(So./DQO);
plot(X,Y,'o-k');
title("Datos experimentales (primer orden)");
xlabel("Tiempo (h)");
ylabel("ln(mg/L)");
grid;
hold on;
pause;