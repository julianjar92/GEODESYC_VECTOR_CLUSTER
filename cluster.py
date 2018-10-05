# -*- coding: utf-8 -*-
"""
NOTA: los archivos de velocidad deben ser de formato csv (texto delimitado por comas)
EJ:
Estacion,Longitud,Latitud,Evel,Nvel,Uvel,Magnitud,Direccion,
ABCC,-74.126925,4.661227,-1.28,16.89,-26.2,16.93843263,355.6661529
ABPD,-74.098864,4.476554,0.76,15.9,0.36,15.91815316,2.73658335
ABPW,-73.995111,4.689564,2.71,15.3,1.78,15.53814983,10.04429297

NOTA2: Se debera especificar la ruta donde se encuentra el archivo y el tipo de codigicacion
que usa el sistema, en este caso utf-8

NOTA3: los resultados seran generados en un archivo de texto en la misma ubicacion del script .py
dichos resultados seran los datos originales clasificados por grupos de comportamiento de los vectores
de desplazamiento de cada estacion.

los grupos generados son 4: 0,1,2,3
estos describen 4 tipos de comportamientos diferentes
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn import datasets
from sklearn.cluster import KMeans

out = open('clustering_result2.txt','w')
vectores = pd.read_csv('C:/Users/JulianJar92/Documents/GitHub/GEODESYC_VECTOR_CLUSTER/DATA_IN.csv',encoding='utf-8')  ## LECTURA DEL ARCHIVO CON LOS DATOS A TRABAJAR

data = vectores[['Longitud','Latitud','Evel','Nvel','Uvel','Magnitud','Direccion']]         ## EXTRACCION DE DATOS DEL DATAFRAME VECTORES A LA VARIABLE evel
names = vectores['Estacion']

km = KMeans(n_clusters=4, max_iter=3000)                                                    ## Definicion de caracteristicas del metodo clustering
km.fit(data)
labels = km.predict(data)
centroids = km.cluster_centers_
grupos = pd.Series(labels, name='grupo')
print(centroids)
result = pd.concat([names,data, grupos], axis=1)
print(result)
out.write(str(result))
out.close()