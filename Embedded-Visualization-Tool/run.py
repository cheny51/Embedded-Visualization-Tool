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
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

# this is needed for the menu and to quit
from PyQt5.QtWidgets import QAction, qApp


class Embedded_Visualization_Tool(QMainWindow):

    def __init__(self):

        # grabbing the attribute
        super().__init__()

        # configure the title and the size of the window
        self.setWindowTitle('Embedded Visualization Tool')
        self.setGeometry(40, 100, 800, 600)

        # set up menu bar
        self.MenuBarSetting()

        # render this window
        self.show()

    def MenuBarSetting(self):
        '''This method is created to configure the menu bar
        below the main application window.

        '''
        # The menu bar
        menubar = self.menuBar()

        # The "file" menu
        fileMenu = menubar.addMenu('&File')

        # The "exit" item under the "file" menu
        exit_prog = QAction('&Exit', self)
        exit_prog.setShortcut('Ctrl+Q')
        exit_prog.setToolTip('Exit application')
        exit_prog.triggered.connect(qApp.quit)

        # adding the "exit" action under the "file"
        fileMenu.addAction(exit_prog)

        # The "help menu"
        helpMenu = menubar.addMenu('Help')

        # The "about" item under the "help menu"
        about_prog = QAction('About Us', self)

        about_prog.triggered.connect(self.AboutUsPopUp)

        # add the action
        helpMenu.addAction(about_prog)

    def AboutUsPopUp(self):
        message = "Thank you for using this app, this is created by Aiden C. "
        QMessageBox.about(self, "About Us",
                          message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Embedded_Visualization_Tool()
    sys.exit(app.exec_())
