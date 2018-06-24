import pandas as pd
import time
from datetime import date,timedelta

class Data:
    def __init__(self):
        self.Time = self.getTime()
        self.df = self.getData(self.Time)
        self.df_tpex = self.getData_tpex(str(int(self.Time)-19110000))

    def isClose(self):
        if time.localtime().tm_hour >= 14:
                return True
        return False

    def isWeekend(self):
        if time.localtime().tm_wday == 5:
            return 1
        elif time.localtime().tm_wday == 6:
            return 2
        return False

    def getTime(self):
        Weekend = self.isWeekend()
        if Weekend:
            Friday =  date.today()-timedelta(Weekend)
            return Friday.strftime("%Y%m%d")
        elif self.isClose():
            return time.strftime("%Y%m%d")
        else:
            yesterday = date.today() - timedelta(1)
            return yesterday.strftime("%Y%m%d")

    def getData(self,Time):
        url = "http://www.tse.com.tw/exchangeReport/MI_INDEX?response=html&date=%s&type=ALLBUT0999"%Time
        data = pd.read_html(url)[-1]
        data.columns = [col[2] for col in data.columns]
        data = data.set_index("證券代號")
        return data

    def getData_tpex(self,Time):
        url = "http://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=htm&d=%s&s=0,asc,0"%(Time[:-4]+'/'+Time[3:5]+"/"+Time[5:])
        data = pd.read_html(url)[-1]
        data.columns = [col[1] for col in data.columns]
        data = data.set_index("代號")
        return data

    def getStockName(self,stockNum):
        try:
            return self.df.loc[stockNum]["證券名稱"]
        except KeyError:
            try:
                return self.df_tpex.loc[stockNum]["名稱"]
            except Exception:
                return "None"

    def getClosingPrice(self,stockNum):
        try:
            return self.df.loc[stockNum]["收盤價"]
        except KeyError:
            try:
                return self.df_tpex.loc[stockNum]["收盤"]
            except Exception:
                return "0.0"

