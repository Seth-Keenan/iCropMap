import folium
from folium import plugins
import ipywidgets
import geocoder
import geopy
import numpy as np
import pandas as pd

def main():
    map = folium.Map()
    map.save("map.html")

main()