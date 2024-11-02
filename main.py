import sys
from PyQt5 import QtWidgets
from map import Map
from mapWindow import MapWindow
from data import Crop

def main():
    choice = "BARLEY"
    Crop(choice)
    app = QtWidgets.QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
