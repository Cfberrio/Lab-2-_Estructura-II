import sys
import mpu
from geopy import Point
import geopy.distance
import folium
import pandas as pd
import numpy as np
print(sys.setrecursionlimit(4000))
data = pd.read_csv("co.csv")
data_capitals=["capital","lat","lng"]
data_capitals = data.loc[data['capital'].isin(["primary","admin"])]
data_city = data_capitals[["city","lat","lng"]]

m = folium.Map(location=[10.963889,-74.796387], zoom_start=13)
lista = data_city.values.tolist()
for row in lista:
    folium.Marker([row[1], row[2]], popup=row[0]).add_to(m)
m.save("try.html")

data_cords = pd.read_csv("datalab (3).csv")
lista_cords_o= data_cords["Coordenadas.O"].values.tolist()
lista_cords_d = data_cords["Coordenadas D"].values.tolist()
cord1=[]
points = []
lista_cords_o.pop()
lista_cords_o.pop()
for i in range(len(lista_cords_o)):
    cord1=lista_cords_o[i].split(', ')
    lat1 =float(cord1[0])
    lon1 =float(cord1[1])
    points.append([cord1[0], cord1[1]])
folium.PolyLine(points, color = "red").add_to(m)
m.save("try.html")
