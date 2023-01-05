from autobuy import Ui_mainWindow
import autobuy_function
import sys
from PyQt5 import QtCore,QtGui, QtWidgets

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainWindow,self).__init__()
        self.ui=Ui_mainWindow()
        self.ui.setupUi(self)

    def autoshop(self,fb_email,password,phone,email,size,quantity):
        

    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit((app.exec_()))