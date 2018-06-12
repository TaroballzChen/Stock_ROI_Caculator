from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor
import csv,os

class table(QtWidgets.QTableWidget,):

    def __init__(self):
        super(table, self).__init__()
        self.col = ["篩選日期", "股票代號", "證券名稱", "篩選日收盤價", "上市櫃最新價", "報酬率"]
        self.init_table()


    def init_table(self):
        self.currentRowCount = self.rowCount()
        self.setColumnCount(len(self.col))
        self.setHorizontalHeaderLabels(self.col)
        self.databaseOpen()

    def newItem(self,col,text):
        Item = QtWidgets.QTableWidgetItem(text)
        self.setItem(self.currentRowCount,col,Item)

    def calcROI(self,predict_price,real):
        ROI = (float(real) - float(predict_price)) / float(predict_price) * 100
        return "%.2f%%"%ROI

    def ROI_style(self,ROI):
        ROI_item = QtWidgets.QTableWidgetItem(ROI)
        if float(ROI[:-1]) > 0.0:
            ROI_item.setBackground(QColor(111,255,0))
        else:
            ROI_item.setBackground(QColor(255, 0, 0))
        return ROI_item

    """
    Read csv file format as database
    """

    def isExist(self):
        while True:
            self.path = QtWidgets.QFileDialog.getOpenFileName(self, "Open Databases with csv format",os.getenv(os.getcwd()), 'CSV(*.csv)')
            if self.path[0] != "" and self.path[0].endswith(".csv"):
                return True

    def databaseOpen(self):
        if self.isExist():
            with open(self.path[0],newline="") as csv_file:
                self.setRowCount(0)
                self.setColumnCount(len(self.col))
                database = csv.reader(csv_file,dialect='excel')
                for row_data in database:
                    row = self.rowCount()
                    self.insertRow(row)
                    for column, stuff in enumerate(row_data):
                        if column == len(self.col) - 1:
                            item = self.ROI_style(stuff)
                        else:
                            item = QtWidgets.QTableWidgetItem(stuff)
                        self.setItem(row,column,item)

    """
    Write CSV
    """

    def SaveDatabase(self):
        if self.path[0] != "":
            with open(self.path[0],'w') as csv_file:
                writer = csv.writer(csv_file, dialect='excel')
                for row in range(self.rowCount()):
                    row_data = []
                    for column in range(self.columnCount()):
                        item = self.item(row,column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append("")
                    writer.writerow(row_data)