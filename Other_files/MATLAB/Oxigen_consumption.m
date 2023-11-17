% File: Coefficient of oxigen consumption
% Author: Luis David Rodriguez Centeno
% License: MIT

% Experimental values
q = [0.235 0.179 0.143];
VUO = [0.1837 0.1038 0.0383];
VUO2 = VUO * 1440;
Xva = [692 644 635];
RO2 = VUO2./Xva;

% Experimental data graph
plot(q,RO2,'+')
hold on

% Obtaining tendency line
y2 = polyfit(q,RO2,1);
m2 = y2(1)
b2 = y2(2)
recta2 = q.*m2+b2;
plot(q,recta2)
title('Calculo de a y b')
xlabel('q (d^{-1})')
ylabel('RO2 (d^{-1})')

% Coefficient values
a = m2
b = b2

% Mean Square Error
MSE = sum((RO2 -recta2).^2) / length(RO2)