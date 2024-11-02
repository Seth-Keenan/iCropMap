import sys
from PyQt5 import QtWidgets
from map import Map
from mapWindow import MapWindow
from index import IndexWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    indexWindow = IndexWindow()
    indexWindow.show()
    if False:
        mapWindow = MapWindow()
        mapWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
