import folium
from folium.plugins import MiniMap
import tkinter as tk
from tkinter import ttk
import requests
import pandas

class Map:
    def __init__(self):
        #self.crop = crop
        self.m = folium.Map(
            location=(39.30, -98.5795),
            zoom_start=5,
            min_zoom = 5,
            max_zoom = 7,
            min_lat=24.396308,
            max_lat=49.384358,
            min_lon=-125.0,
            max_lon=-66.93457,
            max_bounds = True,
            scrollWheelZoom=False
        )
        
        self.state_geo = requests.get(
        "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"
        ).json()

        self.m.save("static/map.html")

    def heat_map(self, crop):
        state_data = pandas.read_csv("crop_data.csv")
        
        folium.Choropleth(
            geo_data=self.state_geo,
            name="choropleth",
            data=state_data,
            columns=["State", "Amount"],
            key_on="feature.id",
            fill_color="YlGn",
            fill_opacity=0.7,
            line_opacity=0.5,
            legend_name=crop,
        ).add_to(self.m)

        self.m.save("static/map.html")

    
