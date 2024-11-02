import folium
from folium.plugins import MiniMap
import tkinter as tk
from tkinter import ttk

class Map:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Map")

        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.map_frame = ttk.Frame(root)
        self.map_frame.place(x=0, y=0, width=800, height=600)


        self.m = folium.Map(location=[51.5074, -0.1278], zoom_start=10)
        self.mini_map = MiniMap()
        self.m.add_child(self.mini_map)
        self.m.save('map.html')

        self.show_in_browser()

    def dislay(self):
        import webbrowser
        webbrowser.open('map.html')

    