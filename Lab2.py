import folium
import pandas as pd
import numpy as np
data = pd.read_csv("co.csv")
data_capitals=["capital","lat","lng"]
data_capitals = data.loc[data['capital'].isin(["primary","admin"])]
print(data_capitals)
data_city = data_capitals[["city","lat","lng"]]


m = folium.Map(location=[10.963889,-74.796387], zoom_start=13)

lista = data_city.values.tolist()
for row in lista:
    folium.Marker([row[1], row[2]], popup=row[0]).add_to(m)
m.save("try.html")

data_v = pd.read_csv("vuelos.csv")
