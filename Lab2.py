import collections
import mpu
from geopy import Point
import geopy.distance
import folium
import pandas as pd
import numpy as np
import haversine as hs
data = pd.read_csv("co.csv")
data_capitals=["capital","lat","lng"]
data_capitals = data.loc[data['capital'].isin(["primary","admin"])]
data_city = data_capitals[["city","lat","lng"]]

m = folium.Map(location=[10.963889,-74.796387], zoom_start=13)

lista = data_city.values.tolist()
for row in lista:
    folium.Marker([row[1], row[2]], popup=row[0]).add_to(m)
m.save("try.html")
#Creamos una deque para meter las distancias
distancias = collections.deque()

#Abrimos el .csv con pandas
distance_dt = pd.read_csv("distancia_v.csv")
print(distance_dt.index)

#Iteramos entre las filas de las columnas especificadas para guardar las dos locaciones y poder usar haversine para conseguir la distancia
for i in range(len(distance_dt)):
    loc1=(distance_dt.iloc[i]["Latitud origen   "], distance_dt.iloc[i]["Longitud origen "])
    loc2=(distance_dt.iloc[i]["latitud destino "], distance_dt.iloc[i]["longitud destino"])
    #Metemos la distancia en la deque
    distancias.append(hs.haversine(loc1,loc2))

print(distancias)
