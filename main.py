from PyQt5 import QtWidgets
from ui.ui_op import MainUI
from ui.menubar import Menu
import sys

class window(QtWidgets.QMainWindow,Menu):
    def __init__(self):
        self.MainUI = MainUI()
        super(window, self).__init__()
        self.init_UI()

    def init_UI(self):
        self.setGeometry(100, 100, 650, 500)
        self.setCentralWidget(self.MainUI)
        self.setWindowTitle("報酬率計算")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = window()
    w.show()
    sys.exit(app.exec_())