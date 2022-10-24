import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# QEventloop가 필요한 이유 (balance가 없음)
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.timer = QTimer(self)
        self.timer.singleShot(3000, self.login_callback)
        self.check_balance()

    def login_callback(self):
        self.balance = 100

    def check_balance(self):
        print(self.balance)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()     # main event loop