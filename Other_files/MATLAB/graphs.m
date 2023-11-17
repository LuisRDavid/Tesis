% File: Monod modeling graphs
% Author: Luis David Rodriguez Centeno
% License: MIT
clear
clc

% Initial conditions
r1 = [236 563 5.62]; %[So(mg/L) Xo(SSV(mg/L)) O2i(mg/L)]
r2 = [545 236 4.73]; %[So(mg/L) Xo(SSV(mg/L)) O2i(mg/L)]
time = [0 20]; % Operation time

% Modeling with ODE45 function
[t1,x1] = ode45(@monod, time, r1); %Solving ecuations for Reactor 1
[t2,x2] = ode45(@monod, time, r2); %Solving ecuations for Reactor 2

% Generating graphs for each reactor
close all
    % Reactor 1
name1 = "% [So(mg/L) Xo(SSV(mg/L)) O2i(mg/L)]";
figure(1,"Name",name1)
plot(t1,x1(:,2),'Marker','o', 'Color', "r")