import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Work Scheduler")
        self.setGeometry(300, 300, 400, 400)
        self.setWindowIcon(QIcon("img/icon.png"))
        self.button()

    def button(self):
        btn = QPushButton(text="버튼", parent=self)
        btn.move(10,10)
        

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()