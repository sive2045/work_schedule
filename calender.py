import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


StyleSheet = """
#qt_calendar_navigationbar {
    background-color: rgb(0, 188, 212);
    min-height: 100px;
}


#qt_calendar_prevmonth, #qt_calendar_nextmonth {
    border: none; 
    margin-top: 64px;
    color: white;
    min-width: 36px;
    max-width: 36px;
    min-height: 36px;
    max-height: 36px;
    border-radius: 18px; 
    font-weight: bold; 
    qproperty-icon: none; 
    background-color: transparent;
}
#qt_calendar_prevmonth {
    qproperty-text: "<"; 
}
#qt_calendar_nextmonth {
    qproperty-text: ">";
}
#qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {
    background-color: rgba(225, 225, 225, 100);
}
#qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {
    background-color: rgba(235, 235, 235, 100);
}


#qt_calendar_yearbutton, #qt_calendar_monthbutton {
    color: white;
    margin: 18px;
    min-width: 60px;
    border-radius: 30px;
}
#qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {
    background-color: rgba(225, 225, 225, 100);
}
#qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {
    background-color: rgba(235, 235, 235, 100);
}


#qt_calendar_yearedit {
    min-width: 50px;
    color: white;
    background: transparent;
}
#qt_calendar_yearedit::up-button { 
    width: 20px;
    subcontrol-position: right;
}
#qt_calendar_yearedit::down-button { 
    width: 20px;
    subcontrol-position: left; 
}


CalendarWidget QToolButton QMenu {
     background-color: white;
}
CalendarWidget QToolButton QMenu::item {
    padding: 10px;
}
CalendarWidget QToolButton QMenu::item:selected:enabled {
    background-color: rgb(230, 230, 230);
}
CalendarWidget QToolButton::menu-indicator {
    /*image: none;
    subcontrol-position: right center;
}


#qt_calendar_calendarview {
    outline: 0px;
    selection-background-color: rgb(0, 188, 212);
}
"""


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
        self.initUI()
    
    def initUI(self):
        self.setStyleSheet(StyleSheet)

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