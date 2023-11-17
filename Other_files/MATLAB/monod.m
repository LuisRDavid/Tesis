% File: Reactor Modeling function
% Author: Luis David Rodriguez Centeno
% License: MIT

% Ecuations for the system:
    % Sustract consumption
        % dS/dt = -(umax/Y)(X*Se/Ks+Se)
    % Biomass growth
        % dX/dt = umax * (Se*X/Ks+Se) - kd * X
    % Oxygen consumption
        % dO2/dt = kla(O2sat-O2)-(a/Y) * X * umax * (Se/Ks+Se) + b * X

function dx=monod(t,x)
    umax = 0.7637; 
    a = 3.165;
    b = -0.3539; %d-1
    Ks = 14.4375; %mg/L
    kd = -0.01374; %d-1
    kla = 420.7680; %d-1
    Y = 3.0490;
    O2sat = 7; %mg/L

    dx = zeros(3,1);
    dx(1) = -((umax/Y)*x(1)*x(2))/(Ks+x(1));
    dx(2) = (umax * x(1)* x(2))/(Ks+x(2)) - kd * x(2);
    dx(3) = kla * (O2sat-x(3))-(((a/Y) * umax * x(2) * x(1))/(Ks+x(1))) - b * x(2);
end