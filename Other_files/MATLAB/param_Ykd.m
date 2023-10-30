% Experimental data

q = [0.235 0.179 0.143];
mu = [0.571 0.429 0.286];

% Experimental data graph
plot(q,mu,'or')
hold on
y1 = polyfit(q,mu,1);
m1 = y1(1)
b1 = y1(2)

% Graphing adjusted tendency line
recta1 = q.*m1+b1;
plot(q,recta1)
title('Cálculo de Y y kd')
xlabel('q(d^{-1})')
ylabel('U(d^{-1})')
grid

% Coefficient values
Y = m1
kd = b1

% Mean Square Error
MSE = sum((mu-recta1).^2) / length(mu)