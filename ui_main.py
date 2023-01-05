import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer
from src.ui_loader import *
from src.utils import *

# connect UI
ui_auto_complete("src/main.ui", "src/main_ui.py")
from src.main_ui import Ui_MainWindow

class MyWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # load UI
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Work Scheduler")
        self.setWindowIcon(QIcon("img/icon.png"))
        self.set_status_bar()

        self.set_sttich_image()
        self.set_today_label()

        self.set_timer()
        self.main_ui.work_start.clicked.connect(self.work_start_btn)
        self.main_ui.work_end.clicked.connect(self.work_end_btn)


    def set_status_bar(self):
        self.main_ui.statusbar.showMessage("WORK SCHDULER v1.0")

    def set_sttich_image(self, work=False):
        if work:
            self.main_ui.sttich.setPixmap(QPixmap("img/sttich_work.png"))
        else:    
            self.main_ui.sttich.setPixmap(QPixmap("img/sttich_happy.png"))
    
    def set_today_label(self):
        _day = what_day_is_today()
        self.main_ui.today_label.setText(_day)

    def set_timer(self):
        self.main_ui.work_timer.display('00:00')       

        self.timer = QTimer()
        self.timer.setInterval(1000) # interval 1 min
        self.timer.timeout.connect(self.timeout)

        # Init buttons
        self.main_ui.work_start.setEnabled(True)
        self.main_ui.work_end.setEnabled(False)
 
    def work_start_btn(self):
        # on/off btn
        self.main_ui.work_start.setEnabled(False)
        self.main_ui.work_end.setEnabled(True)

        # Change sttich img
        self.set_sttich_image(work=True)
        
        # Turn on Timer
        self.min_time = 0
        self.hour_time = 0
        self.timer.start()       
    
    def work_end_btn(self):
        # stop timer
        self.timer.stop()

        # on/off btns
        self.main_ui.work_start.setEnabled(True)
        self.main_ui.work_end.setEnabled(False)

        # Change sttich img
        self.set_sttich_image(work=False)

        # alter massage 
        QMessageBox.about(self, "WORK TIME", f"Work time : {str(self.hour_time).rjust(2,'0')}:{str(self.min_time).rjust(2,'0')}")
        self.min_time = 0
        self.hour_time = 0
        self.main_ui.work_timer.display(f"{str(self.hour_time).rjust(2,'0')}:{str(self.min_time).rjust(2,'0')}")

    def timeout(self):
        self.min_time += 1
        if self.min_time >= 60:
            self.min_time = 0
            self.hour_time += 1 # TBD: 24시간 넘어갈 시 예외 처리 필요

        sender = self.sender()
        if id(sender) == id(self.timer):
            self.main_ui.work_timer.display(f"{str(self.hour_time).rjust(2,'0')}:{str(self.min_time).rjust(2,'0')}")

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = MyWindow() 

    myWindow.show()

    app.exec_()