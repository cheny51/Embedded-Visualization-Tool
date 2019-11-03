'''
The purpose of this script is to create the
basic architecture of the application GUI， which
includes the following:

#. the window title
#. the window size

Creator: Aiden Chen  
'''
# standard libraries
import sys

# third party libraries
from PyQt5.QtWidgets import QApplication, QtWidget
# from PyQt5.QtGui import QIcon

class Embedded_Visualization_Tool(QtWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Embedded Visualization Tool')
        self.setGeometry(10, 10, 400, 600)
        self.show()