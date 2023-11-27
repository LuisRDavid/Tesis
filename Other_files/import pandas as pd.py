#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 21:29:33 2023

@author: luisrc
"""

from cProfile import label
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Metadata/6.3.1_es/conjunto_de_datos/6.3.1_sh_es.csv')
time = df['Periodo']
values = df['Proporción de aguas residuales tratadas de manera adecuada']

x = np.linspace(1998, 2022, 25)
x1 = x.astype(int)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(time, values, 'o', color='brown', mec='crimson')
ax.plot(time, values, '-', color='sienna')
ax.set_xticks(np.arange(1998, 2023, 1), x1)
ax.set_xlabel('Periodo')
ax.set_ylabel('Porcentaje de aguas tratadas')
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45)
plt.title('Proporción de aguas residuales tratadas de manera adecuada')
plt.show()