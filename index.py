import os
from map import Map
from PyQt5 import QtWidgets, QtWebEngineWidgets, QtCore

class IndexWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("iCROP Map")
        self.setGeometry(100, 100, 1600, 800)

        # Set up the QWebEngineView to display the map
        self.browser = QtWebEngineWidgets.QWebEngineView()
        index_file_path = os.path.join(os.path.dirname(__file__), "index.html")
        self.browser.setUrl(QtCore.QUrl.fromLocalFile(index_file_path))

        # Set the browser widget as the central widget of the window
        self.setCentralWidget(self.browser)