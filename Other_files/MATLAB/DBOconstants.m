clear all
close all
inversoS = [1.11 0.077 0.054];
inversoQ = [4.90 8.40 12.19];

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
%axis([0.07 0 1.5])
grid

qmax = 1/b
Ks = qmax * m

ecm = sum((inversoQ-recta).^2)/length(inversoQ)