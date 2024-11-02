import folium
from folium.plugins import MiniMap
import tkinter as tk
from tkinter import ttk

class Map:
    def __init__(self):
        self.m = folium.Map(location=(39.30, -98.5795), zoom_start=5)
        self.mini_map = MiniMap()
        self.m.add_child(self.mini_map)
        self.m.save('map.html')


    