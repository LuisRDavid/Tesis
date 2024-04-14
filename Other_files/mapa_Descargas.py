import matplotlib.pyplot as plt 
import matplotlib.colors as mplc 
import matplotlib.ticker as ticker 
import pandas as pd
import geopandas as gpd

shapefile = gpd.read_file('Shapefile - Estados/u_territorial_estados_mgn_inegi_2013.shp')
puntos_desecho = pd.read_csv('Puntos_descarga.csv',encoding='utf-8')

shapefile = shapefile.merge(
    right = puntos_desecho,
    left_on = 'nom_ent',
    right_on = 'Entidad Federativa',
    how = 'left'
)

labels = ['de 0 a menos de 140', 'de 140 a menos de 290','de 290 a menos de 430','de 430 a menos de 570','más de 570']

#creando columna con variables categoricas a partir de 'CHOQUE'
shapefile['Puntos de descarga totales_Cuartiles'] = pd.cut(
    x = shapefile['Puntos de descarga totales'],
    bins = 5, 
    labels = labels
    )


#utilizando matplotlib nuevamente
fig , ax = plt.subplots(1, figsize = (14,8))

#definiendo caracteristicas del mapa (categorical = True)
shapefile.plot(
    column = 'Puntos de descarga totales_Cuartiles', 
    categorical = True, 
    legend = True,
    cmap = 'Oranges',
    ax = ax,
    linewidth = 1,
    edgecolor = 'black',
    )

ax.set_title(
    'Puntos de descarga de aguas residuales',
    fontsize = 25
    ) 

ax.axis('off')
fig.show()
fig.savefig('DescargasTotales', format='svg')