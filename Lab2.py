import webbrowser
from flask import Flask, render_template,request
import folium
import pandas as pd
import numpy as np
from select import select

app = Flask (__name__)
@app.route("/data")
def index():
    return render_template('index.html')

@app.route("/data", methods=["GET","POST"])
def VALUE():
    Origin = request.form['Origen']
    
    return render_template('index.html')

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000",1)
    app.run(debug=True)


df = pd.read_csv("datalab (3).csv")
origenes = df["Ciudad Origen"].tolist()
destinos = df['Ciudad Destino'].tolist()
cO = df['Coordenadas.O'].tolist()
cD = df['Coordenadas D'].tolist()
capitales = list(dict.fromkeys(origenes))
capitales.pop()
lat1 = []
lon1 = []
Marker = []

origenes2 = list(set(cO))
origenes2.pop(0)
for j in range(len(capitales)):
    cord1 = origenes2[j].split(', ')
    lat1 = (float(cord1[0]))
    lon1 = (float(cord1[1]))
    Marker.append([capitales[j], lat1, lon1])

mapObj = folium.Map(location=[10.963889, -74.796387], zoom_start=5.2)
mapObj.get_root().html.add_child(folium.Element("""
<!DOCTYPE html>
<html>
<head>
    <h1 id="tittle">RUTA DE VUELOS NACIONALES</h1>
</head>
<body>
    <div>
    <form action="/data" method = "post">
        <label for = "Origen">Escoja la ciudad de Origen:</label>
        <select name="Origen" id="Origen" required>
        <option disabled ="">Selecciona una opcion</option>
            <option value = "ARAUCA - MUNICIPIO">Arauca</option>
            <option value = "ARMENIA">Armenia</option>
            <option value = "BARRANQUILLA">Barranquilla</option>
            <option value = "BOGOTA">Bogota</option>
            <option value = "BUCARAMANGA">Bucaramanga</option>
            <option value = "CALI">Cali</option>
            <option value = "Cartagena">Cartagena</option>
            <option value = "CUCUTA">Cucuta</option>
            <option value = "FLORENCIA">Florencia</option>
            <option value = "IBAGUE">Ibague</option>
            <option value = "LETICIA">Leticia</option>
            <option value = "MANIZALES">Manizales</option>
            <option value = "MEDELLIN">Medellin</option>
            <option value = "MITU">Mitu</option>
            <option value = "MONTERIA">Monteria</option>
            <option value = "NEIVA">Neiva</option>
            <option value = "PASTO">Pasto</option>
            <option value = "PEREIRA">Pereira</option>
            <option value = "POPAYAN">Popayan</option>
            <option value = "PUERTO CARRENO">Puerto carreño</option>
            <option value = "QUIBDO">Quibdo</option>
            <option value = "SAN ANDRES - ISLA">San andres</option>
            <option value = "SAN JOSE DEL GUAVIARE">San josé del guaviare</option>
            <option value = "SANTA MARTA">Santa Marta</option>
            <option value = "VALLEDUPAR">Valledupar</option>
            <option value = "VILLAVICENCIO">Villavicencio</option>
            <option value = "YOPAL">YOPAL</option>
        </select>>
        <input type="submit" value="submit">
     </form>
    
   
    </div>
</body>
<style>html, body {position: absolute;top:80px;left: 150px;width: 50%;height: 75%;margin: 0;padding: 0;}</style>
    <style>#map {position:relative;top:0;bottom:0;right:0px;left:0}</style>
            <style>
                #map_5e554ca4bef32fb1a06204d74aa08df5 {
                    position: right;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 30.0%
                }
            </style>
    
    <style>
        h1 {
            position : relative;
            bottom: 60px;
            text-align: center;
            font-size: 50px;
            background-color: #0abab5;
            font-family: 'Merriweather', serif;
            }
        div{
            position: relative;
            left: 400px;
        }
        button{
            position : relative;

        }
    </style>
"""
                                                ))
for row in Marker:
    folium.Marker([row[1], row[2]]).add_to(mapObj)
mapObj.save("web\\index.html")


lista_cords_o = df["Coordenadas.O"].values.tolist()
lista_cords_d = df["Coordenadas D"].values.tolist()
cord1 = []
points = []
lista_cords_d.pop()
lista_cords_d.pop()
for i in range(len(lista_cords_d)):
    cord1 = lista_cords_d[i].split(', ')
    lat1 = float(cord1[0])
    lon1 = float(cord1[1])
    points.append([lat1, lon1])
    #folium.PolyLine(points, color ="red").add_to(m)
# m.save("try.html")
