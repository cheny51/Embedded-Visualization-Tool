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
from PyQt5.QtWidgets import QApplication, QMainWindow

# this is needed for the menu and to quit
from PyQt5.QtWidgets import QAction, qApp


class Embedded_Visualization_Tool(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Embedded Visualization Tool')
        self.setGeometry(40, 100, 800, 600)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Embedded_Visualization_Tool()
    sys.exit(app.exec_())
