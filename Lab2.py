import mpu
from geopy import Point
import geopy.distance
import folium
import pandas as pd
import numpy as np
data = pd.read_csv("co.csv")
data_capitals=["capital","lat","lng"]
data_capitals = data.loc[data['capital'].isin(["primary","admin"])]
data_city = data_capitals[["city","lat","lng"]]

m = folium.Map(location=[10.963889,-74.796387], zoom_start=13)

lista = data_city.values.tolist()
for row in lista:
    folium.Marker([row[1], row[2]], popup=row[0]).add_to(m)
m.save("try.html")


distance_dt = pd.read_csv("distancia_v.csv")
print(distance_dt.index)
for index, row in distance_dt.iterrows():
    lista= [mpu.haversine_distance((distance_dt["Latitud origen   "], distance_dt["Longitud origen "]), (distance_dt["latitud destino "], distance_dt["longitud destino"]))]

