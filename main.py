import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class MyWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Work Scheduler")
        self.setGeometry(300, 300, 400, 400)
        self.setWindowIcon(QIcon("img/icon.png"))
        self.set_status_bar()

        self.test_line()

        self.set_text_label()
        self.set_sttich_image()

        self.claer_button()
        self.quit_button()
        self.saving_data()

    def set_status_bar(self):
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.statusbar.showMessage("WORK SCHDULER v1.0")

    def saving_data(self):
        btn = QPushButton(text="Save", parent=self)
        btn.move(130, 100)
        btn.clicked.connect(self.saving)
    
    def saving(self):
        data = self.line_edit.text()
        print(f"Input data : {data}")

    def test_line(self):
        self.line_edit = QLineEdit("  ", self)
        self.line_edit.move(10, 100)

    def set_text_label(self):
        self.label = QLabel("Message:", self)
        self.label.move(10,10)
    
    def set_sttich_image(self):
        self.sttich_label = QLabel()
        self.sttich_label.setPixmap(QPixmap("img/sttich.png"))
        self.setCentralWidget(self.sttich_label)

    def claer_button(self):
        btn = QPushButton(text="Claer Label", parent=self)
        btn.move(100,10)
        btn.clicked.connect(self.clear)
    
    def clear(self):
        self.label.clear()
        self.label.setText("Clicked Button")
    
    def quit_button(self):
        btn = QPushButton(text="Quit", parent=self)
        btn.move(10,40)
        btn.clicked.connect(self.close)

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()