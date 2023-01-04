import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

# connect UIC
from_class = uic.loadUiType("main.ui")[0]

class MyWindow(QMainWindow, from_class):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Work Scheduler")
        self.setWindowIcon(QIcon("img/icon.png"))
        self.set_status_bar()
        self.set_sttich_image()

    def set_status_bar(self):
        self.statusbar.showMessage("WORK SCHDULER v1.0")

    def set_sttich_image(self):
        self.sttich.setPixmap(QPixmap("img/sttich_happy.png"))

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = MyWindow() 

    myWindow.show()

    app.exec_()