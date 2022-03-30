__author__ = 'Sanchayan'

import sys
from  PyQt4 import QtGui,QtCore

def fun_wd_Qt():
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QWidget()
    window.setGeometry(150,150,500,300)
    window.setWindowTitle("PyQt tuts")
    window.show()
    sys.exit(app.exec_())


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(150,150,500,300)
        self.setWindowTitle("PyQt tuts")
        self.setWindowIcon(QtGui.QIcon('C:\\Users\Public\Pictures\Sample Pictures\Desert.jpg'))

        #Menu With buttons
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(self.action())

        BillaMenu = mainMenu.addMenu('&Billa')
        #BillaMenu.clicked.connect(self.question_popup())
        RandiMenu = mainMenu.addMenu('&Randi')
        self.statusBar()
        #self.show()
        self.Button()

    # The Quit Button as a Function
    def Button(self):
        btm = QtGui.QPushButton('Quit',self)
        btm.clicked.connect(self.close_application)
        btm.resize(btm.minimumSizeHint())
        btm.move(0,100)
        self.show()



    def close_application(self):
        print("whooaaaa so custom!!!")
        #sys.exit()

    # On a Menu or a Butto click this eill get dispalyed with func called if needed
    def action(self):
        extractAction = QtGui.QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)
        return extractAction

    def question_popup(self):
        choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "Get into the chopper?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass


if __name__ == '__main__':
   # fun_wd_Qt()
    app =  QtGui.QApplication(sys.argv)
    a = Window()
    sys.exit(app.exec_())
