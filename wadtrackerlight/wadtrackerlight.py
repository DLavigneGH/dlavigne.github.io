import sys

from PySide6.QtWidgets import QApplication
from wad_randomizer import DoomWadRandomizer

def main():
    app = QApplication(sys.argv)
    window = DoomWadRandomizer()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()