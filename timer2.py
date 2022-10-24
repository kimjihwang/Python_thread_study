import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import datetime

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.btn = QPushButton("missile 발사", self)
        self.btn.clicked.connect(self.fire)

    def fire(self):
        QTimer.singleShot(5000, self.missile)
        print("missile 발사", datetime.datetime.now())

    def missile(self):
        print("missile 폭발 ", datetime.datetime.now())

print (__name__)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()