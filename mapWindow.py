import os
from map import Map
from PyQt5 import QtWidgets, QtWebEngineWidgets, QtCore

class MapWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("iCROP Map")
        self.setGeometry(100, 100, 1600, 800)

        # Create the Folium map
        map_instance = Map()  # This will save the map as 'map.html'

        # Set up the QWebEngineView to display the map
        self.browser = QtWebEngineWidgets.QWebEngineView()
        map_file_path = os.path.join(os.path.dirname(__file__), "map.html")
        self.browser.setUrl(QtCore.QUrl.fromLocalFile(map_file_path))

        # Set the browser widget as the central widget of the window
        self.setCentralWidget(self.browser)