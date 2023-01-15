import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from src.ui_loader import *
from src.utils import *
import datetime as dt

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
        self.setFixedSize(900,600)

        self.set_sttich_image()
        self.set_statis_image()
        self.set_calendar_image()
        self.set_today_label()

        self.set_timer()
        self.main_ui.work_memo.setReadOnly(True)
        self.main_ui.work_start.clicked.connect(self.work_start_btn)
        self.main_ui.work_end.clicked.connect(self.work_end_btn)

        self.set_todo_list()

        self.main_ui.set_time_goal_btn.clicked.connect(self.set_time_goal)
        self.total_time = 0 # (min)
        self.time_goal = 5  # (hour)

    def set_todo_list(self):
        # Enable Menubar
        self.main_ui.todo_list.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        # Generated Menubar
        self.main_ui.todo_list.customContextMenuRequested.connect(self.generate_menu)
        # Enable double clicked event -> edit item
        self.main_ui.todo_list.viewport().installEventFilter(self)

    def eventFilter(self, source:QObject, event:QEvent):    
        if(
            event.type() == QEvent.Type.MouseButtonDblClick and
            event.buttons() == Qt.MouseButton.LeftButton and
            source is self.main_ui.todo_list.viewport()
        ):
            self.edit_todo_item(event.pos())
        
        return super(MyWindow, self).eventFilter(source, event)

    def edit_todo_item(self, pos):
        """
        빈공간 클릭시 todo 추가
        기존 todo 클릭시 수정
        """
        todo_item = self.main_ui.todo_list.itemAt(pos)

        if(todo_item is None):
            self.add_item()
        else:
            text, ok = QInputDialog.getText(self, 'ToDo', f'Edit ToDo: {todo_item.text()}')
            if ok:
                todo_item.setText(text)

    def generate_menu(self, pos):
        if(self.main_ui.todo_list.itemAt(pos) is None):
            self._todo_add_menu = QMenu(self)
            self._todo_add_menu.addAction("Add", self.add_item)
            self._todo_add_menu.exec_(self.main_ui.todo_list.mapToGlobal(pos))
        else:
            self._todo_del_menu = QMenu(self)
            self._todo_del_menu.addAction("Delete",lambda: self.delete_item(pos))            
            self._todo_del_menu.exec_(self.main_ui.todo_list.mapToGlobal(pos))

    def add_item(self):
        text, ok = QInputDialog.getText(self, 'ToDo', 'Add ToDo')
        if ok:
            _todo_item = QListWidgetItem(text)
            _todo_item.setCheckState(Qt.Unchecked)
            self.main_ui.todo_list.addItem(_todo_item)

    def delete_item(self, pos):
        del_item_row = self.main_ui.todo_list.indexAt(pos).row()
        del_item = self.main_ui.todo_list.takeItem(del_item_row)
        self.main_ui.todo_list.removeItemWidget(del_item)

    def set_time_goal(self):
        _time, ok = QInputDialog.getInt(self, 'Time Goal', 'Set Time Goal(h)')
        if ok:
            self.time_goal = _time
    
    def set_status_bar(self):
        self.main_ui.statusbar.showMessage("WORK SCHDULER v1.0")

    def set_sttich_image(self, work=False):
        if work:
            self.main_ui.sttich.setPixmap(QPixmap("img/sttich_work.png"))
        else:    
            self.main_ui.sttich.setPixmap(QPixmap("img/sttich_happy.png"))
    
    def set_statis_image(self):
        self.main_ui.statis_img.setPixmap(QPixmap("img/statis.png"))

    def set_calendar_image(self):
        self.main_ui.calendar_img.setPixmap(QPixmap("img/calendar.png"))

    def set_today_label(self):
        _day = what_day_is_today()
        self.main_ui.today_label.setText(_day)

    def set_timer(self):
        self.main_ui.work_timer.display('00:00')       

        self.timer = QTimer()
        self.timer.setInterval(60*1000) # interval 1 min (60*1000) ms
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

        # save work start time data -> database
        self.main_ui.work_memo.setReadOnly(False)
        self.work_start_time_date = dt.datetime.now()
        _work_start_time_date = f"{self.work_start_time_date.date()}:{self.work_start_time_date.time()}".split('.')[0]
        self.db_id = db_insert_work_start_time(self.time_goal, _work_start_time_date)
        
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

        # change sttich img
        self.set_sttich_image(work=False)

        # save work end time date -> database
        self.work_end_time_data = dt.datetime.now()
        _work_end_time_date = f"{self.work_end_time_data.date()}:{self.work_end_time_data.time()}".split('.')[0]
        _memo = self.main_ui.work_memo.toPlainText()
        _delta_time = str(self.work_end_time_data - self.work_start_time_date).split('.')[0]
        db_insert_work_end_time(self.db_id, _memo, _work_end_time_date, _delta_time)
        self.main_ui.work_memo.clear()
        self.main_ui.work_memo.setReadOnly(True)

        # alter massage
        QMessageBox.about(self, "WORK TIME", f"Work time : {str(self.hour_time).rjust(2,'0')}:{str(self.min_time).rjust(2,'0')}")
        self.min_time = 0
        self.hour_time = 0
        self.main_ui.work_timer.display(f"{str(self.hour_time).rjust(2,'0')}:{str(self.min_time).rjust(2,'0')}")

    def timeout(self):
        self.total_time += 1 # (min)
        self.min_time += 1
        if self.min_time >= 60:
            self.min_time = 0
            self.hour_time += 1

        sender = self.sender()
        if id(sender) == id(self.timer):
            # update time lcd
            self.main_ui.work_timer.display(f"{str(self.hour_time).rjust(2,'0')}:{str(self.min_time).rjust(2,'0')}")            
            ach_rate = cal_achievement_rate(self.total_time, self.time_goal)
            self.main_ui.ach_rate_label.setText(ach_rate)

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = MyWindow() 

    myWindow.show()

    app.exec_()