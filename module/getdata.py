import pandas as pd
import time
from datetime import date,timedelta

class Data:
    def __init__(self):
        self.Time = self.getTime()
        self.df = self.getData(self.Time)

    def isClose(self):
        if time.localtime().tm_hour >= 14:
                return True
        return False

    def getTime(self):
        if self.isClose():
            return time.strftime("%Y%m%d")
        else:
            yesterday = date.today() - timedelta(1)
            return(yesterday.strftime("%Y%m%d"))

    def getData(self,Time):
        url = "http://www.tse.com.tw/exchangeReport/MI_INDEX?response=html&date=%s&type=ALLBUT0999"%Time
        data = pd.read_html(url)[-1]
        data.columns = [col[2] for col in data.columns]
        data = data.set_index("證券代號")
        return data

    def getStockName(self,stockNum):
        try:
            return self.df.loc[stockNum]["證券名稱"]
        except:
            return "None"

    def getClosingPrice(self,stockNum):
        try:
            return self.df.loc[stockNum]["收盤價"]
        except:
            return "0.0"

