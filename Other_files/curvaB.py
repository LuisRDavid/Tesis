#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 21:29:33 2023

@author: luisrc
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('/home/luisrc/Documents/Tesis/Other_files/curvaCalibracionB.csv', index_col=0)
xVal = df['CONCENTRACION']
yVal = df['ABS']
linearRegressor = LinearRegression()
linearRegressor.fit(xVal, yVal)
m = linearRegressor.coef_[0][0]
c = linearRegressor.intercept_[0]
plt.plot(xVal, yVal, '-b', ylabel='Abs')
plt.scatter(xVal, yVal, 'bo')
plt.grid()
plt.show()