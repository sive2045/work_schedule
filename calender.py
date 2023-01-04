import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CalendarWidget(QCalendarWidget):

    def __init__(self, *args, **kwargs):
        super(CalendarWidget, self).__init__(*args, **kwargs)
        self.setVerticalHeaderFormat(self.NoVerticalHeader)

        fmtBlack = QTextCharFormat()
        fmtBlack.setForeground(QBrush(Qt.black))
        self.setWeekdayTextFormat(Qt.Saturday, fmtBlack)

        fmtOrange = QTextCharFormat()
        fmtOrange.setForeground(QBrush(QColor(252, 140, 28)))
        self.setWeekdayTextFormat(Qt.Sunday, fmtOrange)


class MyWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.set_style()
        self.initUI()
    
    def set_style(self):
        with open("StyleSheet.txt", 'r') as f:
            self.setStyleSheet(f.read())

    def initUI(self):
        #self.setStyleSheet(StyleSheet)

        cal = CalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)
        self.setCentralWidget(widget)

        self.setWindowTitle("Work Scheduler")
        self.setGeometry(300, 300, 900, 900)
        self.setWindowIcon(QIcon("img/icon.png"))

        self.show()
    
    def showDate(self, date):
        self.lbl.setText(date.toString())

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    window = MyWindow()
    app.exec_()