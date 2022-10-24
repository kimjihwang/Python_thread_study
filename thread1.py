import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


# 멀티스레딩의 기본코드
'''
파이썬에서 스레드를 사용하는 다양한 방법이 있습니다. 이번 절에서는 PyQt의 QThread 클래스를 사용해서 스레드를 생성해보겠습니다. 
QThread 클래스를 상속받는 Worker 클래스를 정의합니다. Worker 메서드는 run이라는 이름의 메서드를 갖습니다. 
run 메서드는 기본적으로 while 문을 사용한 무한 루프 구조를 갖습니다. 무한 루프 내에서는 원하는 작업을 기술하면 됩니다. 
예제에서는 화면에 '안녕하세요'를 출력하도록 했습니다. 무한 루프이기 때문에 해당 작업이 계속 실행될 겁니다. 
따라서 QThread 클래스에 정의된 sleep 메서드를 통해 적당한 시간 동안 스레드가 실행되지 않도록 sleep을 해줍니다. 
예제에서는 1초 동안 sleep 했습니다.
'''
class Worker(QThread):
    def run(self):
        while True:
            print("안녕하세요")
            self.sleep(1)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker = Worker()
        self.worker.start()


app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()