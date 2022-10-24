import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# 스레드 컨트롤
'''
이번에는 실행된 스레드를 멈추고 다시 재실행해 보겠습니다. 
QThread 클래스에는 스레드를 멈추는 pause( ), 멈춘 스레드를 재 시작하는 resume( ) 메서드가 존재하지 않습니다. 
따라서 사용자가 스레드가 실행되는 run( ) 메서드에서 변수를 사용해서 스레드에 의해 실행되는 코드 부분을 실행되지 않도록 해줘야야 합니다. 
전체 코드는 다음과 같습니다.
'''
class Worker(QThread):
    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        while self.running:
            print("안녕하세요")
            self.sleep(1)

    def resume(self):
        self.running = True

    def pause(self):
        self.running = False


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker = Worker()
        self.worker.start()

        btn1 = QPushButton("resume", self)
        btn1.move(10, 10)
        btn2 = QPushButton("pause", self)
        btn2.move(10, 50)

        # 시그널-슬롯 연결하기
        btn1.clicked.connect(self.resume)
        btn2.clicked.connect(self.pause)

    def resume(self):
        self.worker.resume()
        self.worker.start()

    def pause(self):
        self.worker.pause()


app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()