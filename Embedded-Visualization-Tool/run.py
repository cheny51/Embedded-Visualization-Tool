'''
The purpose of this script is to create the
basic architecture of the application GUI， which
includes the following:

#. the window title
#. the window size
#. the window menubar

Creator: Aiden Chen
'''
# standard libraries
import sys

# third party libraries
from PyQt5.QtWidgets import QApplication

# local libraries
# from name-folder import name-module
from MainGui.main_gui import Embedded_Visualization_Tool

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Embedded_Visualization_Tool()
    sys.exit(app.exec_())
