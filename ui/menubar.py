from PyQt5 import QtWidgets


class Menu():
    def __init__(self):
        self.init_menu()

    def init_menu(self):
        self.bar = self.menuBar()
        self.bar.setNativeMenuBar(False)
        self.MenuFileOption()


    def MenuFileOption(self):
        self.MenuFileOp = self.bar.addMenu("File")

        self.SaveAction = QtWidgets.QAction("Save",self)
        # self.OpenAction = QtWidgets.QAction("Open File",self)
        self.OptionAddAction(self.MenuFileOp, self.SaveAction)

        self.SaveAction.triggered.connect(self.MainUI.table.SaveDatabase)

    def OptionAddAction(self,Option,*ActionList):
        for action in ActionList:
            Option.addAction(action)
