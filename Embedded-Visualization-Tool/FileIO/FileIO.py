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
from PyQt5.QtWidgets import QFileDialog, QFileSystemModel, QListView

from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QDir


class FiloIOTab(QWidget):
    '''This class houses all the set widgets used in the
    fileio tab.

    '''
    def __init__(self):
        '''constructor function of the FiloIO tab.

        '''
        super().__init__()
        self.folder_path = QDir.rootPath()
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
        self.fileio_tab_select_folder_pushbutton = QPushButton('Select Folder Here')
        self.fileio_tab_select_folder_pushbutton.clicked.connect(self.fileio_import_files_from_folder_dialog)

        # File selected directory display box, for display only
        self.fileio_tab_select_folder_lineedit = QLineEdit('')
        self.fileio_tab_select_folder_lineedit.setReadOnly(True)

        # TODO: add in method that open input dialogue box, filter to .csv to import
        # self.fileio_tab_select_folder_pushbutton.clicked.connect(self.fileio_import_files_from_folder_dialog())

        # TODO: add in method that check if the selected file is valid, such as no 
        #       empty file imported

        # Import selected file push button
        self.fileio_tab_import_selected_pushbutton = QPushButton('Import File Within Folder Here')
        self.fileio_tab_import_selected_pushbutton.setFixedWidth(250)
        self.fileio_tab_import_selected_pushbutton.setEnabled(False)
        
        # Import selected file tableview
        self.fileio_tab_import_selected_table = QListView()
        self.fileio_tab_import_selected_table.setFixedHeight(200)
        self.fileio_tab_import_selected_pushbutton.clicked.connect(self.fileio_import_files_from_selected_folder)
        self.fileio_tab_import_selected_fileModel = QFileSystemModel()

        # List out the files in that folder that contains csv
        self.fileio_tab_import_selected_fileModel.setFilter(QDir.NoDotAndDotDot | QDir.Files)
        CSV_FILE_FILTER = ["*.csv"]
        self.fileio_tab_import_selected_fileModel.setNameFilters(CSV_FILE_FILTER)
        self.fileio_tab_import_selected_fileModel.setNameFilterDisables(False)

        self.fileio_tab_import_selected_table.setModel(self.fileio_tab_import_selected_fileModel)
        self.fileio_tab_import_selected_table.setRootIndex(self.fileio_tab_import_selected_fileModel.index(self.folder_path))
        
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

        # Add all import related widgets
        self.fileio_tab_import_layout_grid.addWidget(self.fileio_tab_select_folder_pushbutton, 0, 0)
        self.fileio_tab_import_layout_grid.addWidget(self.fileio_tab_select_folder_lineedit, 0, 1)
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

    def fileio_import_files_from_folder_dialog(self):
        '''This function opens a file dialogue, and it will
        ask user to select a folder to open, and if the folder
        is selected and opened, it search for the .csv just
        in that folder.
        '''
        self.fileio_tab_import_selected_pushbutton.setEnabled(False)
        # configure the input file dialog, dialog window title
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        dialog_box_title = 'Select Directory'
        self.folder_path = QFileDialog.getExistingDirectory(self,
                                                            dialog_box_title)

        # save the folder path if successfully selected
        if self.folder_path:
            self.fileio_tab_select_folder_lineedit.setText(self.folder_path)
            self.fileio_tab_import_selected_pushbutton.setEnabled(True)
            self.fileio_tab_import_selected_label.setText("Import Status: unimported")

    def fileio_import_files_from_selected_folder(self):
        # store the file path
        if (self.folder_path != ""):
            folder_path = self.folder_path
            self.fileio_tab_import_selected_table.setRootIndex(self.fileio_tab_import_selected_fileModel.setRootPath(folder_path))
            self.fileio_tab_import_selected_label.setText("Import Status: imported")