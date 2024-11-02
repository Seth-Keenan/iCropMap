import folium
from folium.plugins import MiniMap
import tkinter as tk
from tkinter import ttk
import requests

class Map:
    def __init__(self):
        self.m = folium.Map(
            location=(39.30, -98.5795), 
            zoom_start=5,
            dragging = False,
            zoom_control = False,
            scrollWheelZoom = False
            )
        
        state_geo = requests.get(
        "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"
        ).json()
        
        folium.Choropleth(
            geo_data=state_geo,
            name="choropleth",
            columns=["State", "Unemployment"],
            key_on="feature.id",
            fill_color="YlGn",
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name="Unemployment Rate (%)",

        )

        self.mini_map = MiniMap()
        self.m.add_child(self.mini_map)
        self.m.save('map.html')


    