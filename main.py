import sys
from PyQt5 import QtWidgets
from map import Map
from mapWindow import MapWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
