import folium
from folium.plugins import MiniMap
import tkinter as tk
from tkinter import ttk
import requests
import pandas

class Map:
    def __init__(self):
        self.m = folium.Map(
            location=(39.30, -98.5795), 
            zoom_start=5,
            dragging = False,
            zoom_control = False,
            scrollWheelZoom = False,
            doubleClickZoom = False
            )
        
        state_geo = requests.get(
        "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"
        ).json()

        state_data = pandas.read_csv("crop_data.csv")
        
        folium.Choropleth(
            geo_data=state_geo,
            name="choropleth",
            data=state_data,
            columns=["State", "Amount"],
            key_on="feature.id",
            fill_color="YlGn",
            fill_opacity=0.7,
            line_opacity=0.5,
            legend_name="Crop",
        ).add_to(self.m)

        self.m.save("map.html")

    
