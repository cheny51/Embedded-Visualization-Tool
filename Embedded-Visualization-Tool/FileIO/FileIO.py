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
from PyQt5.QtWidgets import QWidget, QTableView, QVBoxLayout
from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QIcon


class FiloIOTab(QWidget):
    '''This class houses all the set widgets used in the
    fileio tab.

    '''
    def __init__(self):
        '''constructor function of the FiloIO tab.

        '''
        super().__init__()

        # define outer sturcture of this tab
        self.fileio_layout = QVBoxLayout()

        # file io tab label
        self.fileio_tab_title_label = QLabel()
        self.fileio_tab_title_label.setFont(QFont('Arial', 10))
        self.fileio_tab_title_label.setText('<b>File Import Tab:</b>')
        self.fileio_layout.addWidget(self.fileio_tab_title_label)
        
        # define the inner structure below the header
        self.fileio_tab_layout_grid = QGridLayout()

        # File select button
        self.fileio_tab_select_file_pushbutton = QPushButton('Select File Here')

        # File selected directory display box, for display only
        self.fileio_tab_select_file_lineedit = QLineEdit('')
        self.fileio_tab_select_file_lineedit.setReadOnly(True)

        # TODO: add in method that open input dialogue box, filter to .csv to import
        # TODO: add in method that check if the selected file is valid, such as no 
        #       empty file imported

        # Import selected file push button
        self.fileio_tab_import_selected_pushbutton = QPushButton('Import File Here')
        self.fileio_tab_import_selected_pushbutton.setFixedWidth(250)
        # TODO: add in method that convert csv to a valid dataframe

        # Import selected file tableview
        self.fileio_tab_import_selected_table = QTableView()
        self.fileio_tab_import_selected_table.setFixedHeight(200)

        self.fileio_tab_layout_grid.addWidget(self.fileio_tab_select_file_pushbutton, 0, 0)
        self.fileio_tab_layout_grid.addWidget(self.fileio_tab_select_file_lineedit, 0, 1)
        self.fileio_tab_layout_grid.addWidget(self.fileio_tab_import_selected_pushbutton, 1, 0)
        self.fileio_tab_layout_grid.addWidget(self.fileio_tab_import_selected_table, 1, 1)
        self.fileio_layout.addLayout(self.fileio_tab_layout_grid)
        self.fileio_layout.addStretch(20)

        self.setLayout(self.fileio_layout)
