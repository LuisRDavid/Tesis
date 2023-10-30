% File: Substrate consuption coefficient
% Author: Luis David Rodriguez Centeno
% License: MIT

inversoS = [0.0191 0.0145 0.0501];
inversoQ = [4.241 5.570 6.99];

plot(inversoS,inversoQ,'o');
hold on;

y = polyfit(inversoS,inversoQ,1);
m = y(1);
b = y(2);
recta = inversoS.*m+b;

plot(inversoS,recta);
title('Calculo de qmax y Ks');
xlabel('1/s (L/mg)');
ylabel('1/q (d)');
grid

qmax = 1/b
Ks = qmax * m

ecm = sum((inversoQ - recta).^2) / length(inversoQ)