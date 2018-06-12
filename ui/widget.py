from PyQt5 import QtWidgets
from ui.table import table


class widget(QtWidgets.QWidget,):
    def __init__(self):
        super().__init__()
        self.table = table()


    def search_block(self,run):
        stock_num = QtWidgets.QLabel("股票代號")
        self.stock_num_input = QtWidgets.QLineEdit()

        stock_name = QtWidgets.QLabel("證券名稱")
        self.stock_name  = QtWidgets.QLineEdit()
        self.stock_name.setReadOnly(True)

        predict_price_l = QtWidgets.QLabel("篩選日收盤價")
        self.predict_price = QtWidgets.QLineEdit()

        self.runbutton = QtWidgets.QPushButton("計算")

        box = QtWidgets.QHBoxLayout()
        box.addWidget(stock_num)
        box.addWidget(self.stock_num_input)
        box.addWidget(stock_name)
        box.addWidget(self.stock_name)
        box.addWidget(predict_price_l)
        box.addWidget(self.predict_price)
        box.addWidget(self.runbutton)

        self.runbutton.clicked.connect(run)

        return box

    """
    table block
    """

    def table_block(self):
        box = QtWidgets.QHBoxLayout()
        box.addWidget(self.table)
        return box
