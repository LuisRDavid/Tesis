#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 

@author: luisrc
"""

from matplotlib import legend, legend_handler
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv('Metadata/6.3.1_es/conjunto_de_datos/6.3.1_dc_433_es.csv')
df2 = pd.read_csv('Metadata/6.3.1_es/conjunto_de_datos/6.3.1_dc_431_es.csv')
x = df1['Periodo']
y1 = df1['Caudal de agua residual generada de origen municipal']
y2 = df2['Caudal de agua residual tratada de origen municipal']
x1 = np.linspace(1998, 2022, 25)
ticks = x1.astype(int)

fig, axs = plt.subplots(1, 2, figsize=(12,5.5), layout='constrained')
axs[0].plot(x, y1, 'r-o', label="Caudal de agua residual generada de origen municipal")
axs[0].set_xlabel('Periodo')
axs[0].set_ylabel('Caudal de agua residual generada (m³)')
axs[0].set_xticks(ticks)
axs[0].tick_params(axis='x', labelrotation=90)
axs[1].plot(x, y2, 'g-o', label="Caudal de agua residual tratada de origen municipal")
axs[1].set_xlabel('Periodo')
axs[1].set_ylabel('Caudal de agua residual tratada (m³)')
axs[1].set_xticks(ticks)
axs[1].tick_params(axis='x', labelrotation=90)
axs[0].legend(loc='upper left', title_fontsize='small')
axs[1].legend(loc='upper left', title_fontsize='small')
fig.suptitle('Aguas residuales de origen municipal')
plt.show()
