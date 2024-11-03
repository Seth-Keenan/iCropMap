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

        folium.Choropleth(
            geo_data=self.state_geo
        )

        self.m.save("static/map.html")

    def heat_map(self, crop):
        if(crop == ''):
            folium.Choropleth(
                geo_data=self.state_geo,
                name="choropleth",
                fill_color="lightgray",
                fill_opacity=0.7,
                line_opacity=0.5,
            ).add_to(self.m)

            self.m.save("static/map.html")
        else:
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
                legend_name=f"Acres of {crop.lower()} planted",
                nan_fill_color="lightyellow"
            ).add_to(self.m)

            self.m.save("static/map.html")

        style = lambda x: {
            'fill_opacity': 0.00000000000000001,
            'line_opacity': 0.0,
            "color": "lightgrey"
        }

        highlight_state = lambda x: {
            'color': 'grey',
            'opacity': 0.3,
            'weight': 3
        }

        df = pandas.read_csv('crop_data.csv')
        amtDict = dict(zip(df['State'], df['Amount']))
        for feature in self.state_geo['features']:
            state_id = feature['id']
            state_name = feature['properties']['name']
            print(f"Processing state: {state_name}")
            state_geojson = {
                "type": "FeatureCollection",
                "features": [feature]
            }
        
            try:
                amount = "{:,}".format(amtDict.get(state_id))
            except:
                amount = "Zero"

            # Add the GeoJson object to the map with a popup
            folium.features.GeoJson(
                state_geojson,
                # fill_opacity=0.00000000000000001,
                # line_opacity=0.0,
                # color="lightgrey",
                name=state_name,
                style_function=style,
                highlight_function=highlight_state,
                popup=folium.Popup(state_name + "(" + state_id + "):\n" + amount + f" acres of {crop.lower()}")
            ).add_to(self.m)

            # Save the updated map
        self.m.save("static/map.html")

        
        
        
