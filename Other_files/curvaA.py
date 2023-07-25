#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 21:29:33 2023

@author: luisrc
"""

import pandas as pd
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/home/luisrc/Documents/Tesis/Other_files/curvaCalibracionA.csv', index_col=0)
df.plot(ylabel='Abs')
plt.show()