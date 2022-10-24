import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


# 스레드의 값의 전달
'''
스레드를 사용하면 여러 객체가 동시에 스케쥴링 됩니다. 
이때 한 객체에서 다른 객체로 값을 전달해야 하는 경우가 자주 발생합니다. 
이 경우 앞서 배운 사용자 정의 시그널을 사용할 수 있습니다. 
이번에는 Worker 클래스의 객체에서 MyWindow 클래스의 객체로 값을 전달해보겠습니다. 
전체 코드는 다음과 같습니다. 먼저 실행해보시기 바랍니다.
'''

class Worker(QThread):
    timeout = pyqtSignal(int)    # 사용자 정의 시그널

    def __init__(self):
        super().__init__()
        self.num = 0             # 초깃값 설정

    def run(self):
        while True:
            self.timeout.emit(self.num)     # 방출
            self.num += 1
            self.sleep(1)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker = Worker()
        self.worker.start()
        self.worker.timeout.connect(self.timeout)   # 시그널 슬롯 등록

        self.edit = QLineEdit(self)
        self.edit.move(10, 10)

    @pyqtSlot(int)
    def timeout(self, num):
        self.edit.setText(str(num))


app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()