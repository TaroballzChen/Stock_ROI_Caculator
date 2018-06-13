from ui.widget import widget
from PyQt5 import QtWidgets
from module.getdata import Data

class MainUI(widget):

    def __init__(self):
        self.Data = Data()
        super(MainUI, self).__init__()
        self.init_UI()

    def init_UI(self):
        UI_layout = QtWidgets.QVBoxLayout()
        UI_layout.addLayout(self.search_block(run = self.run))
        UI_layout.addLayout(self.table_block())

        self.setLayout(UI_layout)

    def run(self):
        stockNum = self.stock_num_input.text()
        stockName = self.UI_setStockName(stockNum)
        predict_price = self.predict_price.text()
        ClosingPrice = self.Data.getClosingPrice(stockNum)
        if stockNum != "" and predict_price != "" and stockName != "None":
            try:
                ROI = self.table.calcROI(predict_price,ClosingPrice)
            except ValueError:
                return
            else:
                ROI = self.table.ROI_style(ROI)
                self.updateTable(self.Data.Time,stockNum,stockName,predict_price,ClosingPrice,ROI)


    def UI_setStockName(self,stockNum):
        stockName = self.Data.getStockName(stockNum)
        self.stock_name.setText(stockName)
        return stockName

    def updateTable(self,*Textlist):
        self.table.insertRow(self.table.currentRowCount)
        for Text in Textlist:
            self.table.newItem(Textlist.index(Text), Text)

