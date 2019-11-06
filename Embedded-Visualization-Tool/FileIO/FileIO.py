'''
The purpose of this script is to create the
basic architecture of the application GUI， which
includes the following:

#. the window title
#. the window size

Creator: Aiden Chen  
'''
# standard libraries

# third party libraries
from PyQt5.QtWidgets import QWidget, QTableView, QVBoxLayout, QCheckBox
from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

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
        self.fileio_tab_title_label.setText('<b>File IO Tab</b>')
        self.fileio_layout.addWidget(self.fileio_tab_title_label)

        # define the inner structure below the header
        self.fileio_tab_import_layout_grid = QGridLayout()

        # File select button
        self.fileio_tab_select_file_pushbutton = QPushButton('Select Folder Here')

        # File selected directory display box, for display only
        self.fileio_tab_select_file_lineedit = QLineEdit('')
        self.fileio_tab_select_file_lineedit.setReadOnly(True)

        # TODO: add in method that open input dialogue box, filter to .csv to import
        # TODO: add in method that check if the selected file is valid, such as no 
        #       empty file imported

        # Import selected file push button
        self.fileio_tab_import_selected_pushbutton = QPushButton('Import File Within Folder Here')
        self.fileio_tab_import_selected_pushbutton.setFixedWidth(250)
        # TODO: add in method that convert csv to a valid dataframe

        # Import Status
        # TODO: Add a progress bar, and show a dialogue upon finishes
        self.fileio_tab_import_selected_label = QLabel()
        self.fileio_tab_import_selected_label.setFont(QFont('Arial', 10))
        self.fileio_tab_import_selected_label.setText('Import Status: unimported')

        # Import Configuration Parameters
        self.fileio_tab_import_configuration_layout = QVBoxLayout()

        # Import Configuration File PushButton
        self.fileio_tab_import_configuration_pushbutton = QPushButton("Select Config File")
        # Import Configuration Confirm PushButton
        self.fileio_tab_import_config_confirm_pushbutton = QPushButton("Import Config File")
        # Import Configuration State
        self.fileio_tab_import_config_label = QLabel('No Config Imported')
        self.fileio_tab_import_config_label.setAlignment(Qt.AlignCenter)

        self.fileio_tab_import_configuration_layout.addWidget(self.fileio_tab_import_configuration_pushbutton)
        self.fileio_tab_import_configuration_layout.addWidget(self.fileio_tab_import_config_confirm_pushbutton)
        self.fileio_tab_import_configuration_layout.addWidget(self.fileio_tab_import_config_label)

        # Import selected file tableview
        self.fileio_tab_import_selected_table = QTableView()
        self.fileio_tab_import_selected_table.setFixedHeight(200)

        # Add all import related widgets
        self.fileio_tab_import_layout_grid.addWidget(self.fileio_tab_select_file_pushbutton, 0, 0)
        self.fileio_tab_import_layout_grid.addWidget(self.fileio_tab_select_file_lineedit, 0, 1)
        self.fileio_tab_import_layout_grid.addWidget(self.fileio_tab_import_selected_pushbutton, 1, 0)
        self.fileio_tab_import_layout_grid.addWidget(self.fileio_tab_import_selected_label, 1, 1)
        self.fileio_tab_import_layout_grid.addLayout(self.fileio_tab_import_configuration_layout, 2, 0, Qt.AlignVCenter)
        self.fileio_tab_import_layout_grid.addWidget(self.fileio_tab_import_selected_table, 2, 1)
        self.fileio_layout.addLayout(self.fileio_tab_import_layout_grid)
        self.fileio_layout.addStretch(20)

        # Output Directory Parameters
        self.fileio_tab_export_title_label = QLabel()
        self.fileio_tab_export_title_label.setFont(QFont('Arial', 10))
        self.fileio_tab_export_title_label.setText('<b>Output Directory Parameters: </b>')
        self.fileio_layout.addWidget(self.fileio_tab_export_title_label)

        # Add in the grid for output
        self.fileio_tab_output_layout_grid = QGridLayout()

        # checkbox to enable output graphing plots or not
        self.fileio_tab_export_checkbox = QCheckBox("Save output offline")

        # TODO: add in method to respond to checkbox state
        #       checked: output, enable line editor, unchecked: don't output

        # Select directory to output to
        self.fileio_tab_output_select_directory_pushbutton = QPushButton("Save Plot To Folder...")
        self.fileio_tab_output_select_directory_pushbutton.setFixedWidth(250)
        self.fileio_tab_output_select_directory_lineedit = QLineEdit('')
        self.fileio_tab_output_select_directory_lineedit.setReadOnly(True)
        
        # TODO: add in connect method to add the directory selected to the lineedit


        # Add in all export related widgets
        self.fileio_tab_output_layout_grid.addWidget(self.fileio_tab_export_checkbox, 0, 0)
        self.fileio_tab_output_layout_grid.addWidget(self.fileio_tab_output_select_directory_pushbutton, 1, 0)
        self.fileio_tab_output_layout_grid.addWidget(self.fileio_tab_output_select_directory_lineedit, 1, 1)
        self.fileio_layout.addLayout(self.fileio_tab_output_layout_grid)

        self.setLayout(self.fileio_layout)
