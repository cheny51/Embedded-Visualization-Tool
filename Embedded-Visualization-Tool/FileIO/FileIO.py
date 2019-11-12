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
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QCheckBox
from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtWidgets import QFileDialog, QFileSystemModel, QListView

from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QDir, pyqtSignal, pyqtSlot

# local library import

class FiloIOTab(QWidget):
    '''This class houses all the set widgets used in the
    fileio tab. This class contains 4 attributes that are
    event-driven type of attribute.

    Attributes:
        import_folder_path_selected_state (str): A string message that tells
                                                 whether user selected a folder
                                                 to read .csv from
        file_from_folder_imported_state (str): A string message tells if user
                                               had determined to import .csv
                                               from the imported directory.
        export_folder_path_selected_state (str): A string message tells if user
                                                 had determined a output file
                                                 directory to save graphs
        save_figs (bool): A boolean tells other tabs if the figure needed to be
                          saved offline.
    '''
    # Class attributes
    import_folder_path_selected_state = pyqtSignal(str)
    file_from_folder_imported_state = pyqtSignal(str)
    export_folder_path_selected_state = pyqtSignal(str)
    save_figs = pyqtSignal(bool)

    def __init__(self):
        '''constructor function of the FiloIO tab.

        '''
        super().__init__()
        # Instance variables
        self.import_folder_path = QDir.rootPath()
        self.export_folder_path = QDir.rootPath()
        # signal indicating if something has been successfuly
        # or unsuccessfully operated

        # define outer sturcture of this tab
        self.fileio_layout = QVBoxLayout()

        # file io tab label
        self.fileio_tab_title_label = QLabel()
        self.fileio_tab_title_label.setFont(QFont('Arial', 10))
        self.fileio_tab_title_label.setText('<b>File IO Tab</b>')
        self.fileio_layout.addWidget(self.fileio_tab_title_label)
        # define the inner structure below the header
        self.fileio_tab_import_layout_grid = QGridLayout()
        # widget 1: fileio select folder widget
        self.fileio_import_select_folder_widgets()
        # widget 2: fileio import csv files from folder widget
        self.fileio_import_file_from_folder_widgets()

        # widget 3: fileio import configuration file widget
        # TODO: Unfinished

        # Import Configuration Parameters
        self.fileio_tab_import_configuration_layout = QVBoxLayout()
        # Import Configuration File PushButton
        self.fileio_tab_import_configuration_pushbutton = \
            QPushButton("Select Config File")
        # Import Configuration Confirm PushButton
        self.fileio_tab_import_config_confirm_pushbutton = \
            QPushButton("Import Config File")
        # Import Configuration State
        self.fileio_tab_import_config_label = QLabel('No Config Imported')
        self.fileio_tab_import_config_label.setAlignment(Qt.AlignCenter)
        # Application adding the import parameter widgets onto the application
        self.fileio_import_addwidget()

        # Output Directory Parameters
        self.fileio_tab_export_title_label = QLabel()
        self.fileio_tab_export_title_label.\
            setFont(QFont('Arial', 10))
        self.fileio_tab_export_title_label.\
            setText('<b>Output Directory Parameters: </b>')
        self.fileio_layout.addWidget(self.fileio_tab_export_title_label)
        # Add in the grid for output
        self.fileio_tab_output_layout_grid = QGridLayout()
        # Add in the widgets for the export parameters
        self.fileio_export_select_folder_widgets()
        # Select directory to output to
        self.fileio_export_addwidget()

        self.setLayout(self.fileio_layout)

    def fileio_import_select_folder_widgets(self):
        """Initialize the widgets for folder selection.
        """
        # File select button
        self.fileio_tab_select_folder_pushbutton = QPushButton('Select Folder')
        self.fileio_tab_select_folder_pushbutton.\
            clicked.connect(self.fileio_import_select_folder_directory)

        self.import_folder_path_selected_state.\
            connect(self.folder_path_enable_import_file_widgets)

        # File selected directory display box, for display only
        self.fileio_tab_select_folder_lineedit = QLineEdit('')
        self.fileio_tab_select_folder_lineedit.setReadOnly(True)

    def fileio_import_select_folder_directory(self):
        '''This function opens a file dialogue, and it will
        ask user to select a folder to open, and if the folder
        is imported then, it search for the .csv just
        in that folder.
        '''
        self.fileio_tab_import_selected_pushbutton.setEnabled(False)
        # configure the input file dialog, dialog window title
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        dialog_box_title = 'Select Directory to Read CSV'
        self.import_folder_path = QFileDialog.\
            getExistingDirectory(self, dialog_box_title)

        # save the folder path if successfully selected
        if self.import_folder_path:
            self.import_folder_path_selected_state.\
                emit("Folder selection is successful")

    @pyqtSlot(str)
    def folder_path_enable_import_file_widgets(self, message):
        """This method is called when a folder is successfully
        being imported. And this is where user is allowed to
        load in and select the .csv from that folder

        Args:
            message (str): To check if folder selection is done correctly
        """
        if message == "Folder selection is successful":
            print(message)
            self.fileio_tab_select_folder_lineedit.\
                setText(self.import_folder_path)
            self.fileio_tab_import_selected_pushbutton.setEnabled(True)
            self.fileio_tab_import_selected_label.\
                setText("Import Status: <b>Unimported</b>")

    def fileio_import_file_from_folder_widgets(self):
        """This method initialize the import file from folder widgets
        """
        # Import selected file push button
        self.fileio_tab_import_selected_pushbutton = \
            QPushButton('Import File in this folder')
        self.fileio_tab_import_selected_pushbutton.setFixedWidth(250)
        self.fileio_tab_import_selected_pushbutton.setEnabled(False)

        self.file_from_folder_imported_state.\
            connect(self.fileio_import_enable_csv_file_selection)

        # Import Status
        # TODO: Add a progress bar, and show a dialogue upon finishes
        self.fileio_tab_import_selected_label = QLabel()
        self.fileio_tab_import_selected_label.setFont(QFont('Arial', 10))
        self.fileio_tab_import_selected_label.\
            setText('Import Status: <b>Unimported</b>')

        # Import selected file tableview
        self.fileio_tab_import_selected_table = QListView()
        self.fileio_tab_import_selected_table.setFixedHeight(100)
        self.fileio_tab_import_selected_table.\
            setObjectName('fileio_tab_import_selected_table')

        # When a user click on a cell from the folder
        self.fileio_tab_import_selected_table.clicked.\
            connect(self.select_an_csv_file_from_folder)

        self.fileio_tab_import_selected_pushbutton.\
            clicked.connect(self.fileio_import_files_from_selected_folder)
        self.fileio_tab_import_selected_fileModel = QFileSystemModel()

        # List out the files in that folder that contains csv
        self.fileio_tab_import_selected_fileModel.\
            setFilter(QDir.NoDotAndDotDot | QDir.Files)
        CSV_FILTER = ["*.csv"]
        self.fileio_tab_import_selected_fileModel.\
            setNameFilters(CSV_FILTER)
        # show only the file with the extension .csv
        self.fileio_tab_import_selected_fileModel.\
            setNameFilterDisables(False)

        # TODO: add in method that convert csv to a valid dataframe

    def fileio_import_files_from_selected_folder(self):
        """This method opens and grab all the .csv files that are
        found in the folder that user selected.
        """
        self.fileio_tab_import_selected_table.\
            setModel(self.fileio_tab_import_selected_fileModel)
        # store the file path
        if (self.import_folder_path != ""):
            self.file_from_folder_imported_state.\
                emit("Successful file from folder import")

    @pyqtSlot(str)
    def fileio_import_enable_csv_file_selection(self, message):
        """This method is called when files from the folder
        were successfully displayed in the box. And now the
        user is allowed to select the .csv file they wish to
        analyze.

        Args:
            message (str): To check if file import is done correctly
        """
        if message == "Successful file from folder import":
            print(message)
            folder_path = self.import_folder_path
            self.fileio_tab_import_selected_table.\
                setRootIndex(self.fileio_tab_import_selected_fileModel.
                             setRootPath(folder_path))
            self.fileio_tab_import_selected_label.\
                setText("Import Status: <b>Imported</b>")

    def fileio_export_select_folder_widgets(self):
        # checkbox to enable output graphing plots or not
        self.fileio_tab_export_checkbox = QCheckBox("Save output offline")

        # Method to respond to checkbox state
        self.fileio_tab_export_checkbox.stateChanged.\
            connect(self.fileio_export_file_checkbox_figure_bool)

        # Determine if it's appropriate to save fig
        self.save_figs.connect(self.save_fig_state)

        # Select directory to output to
        self.fileio_tab_output_select_directory_pushbutton = \
            QPushButton("Save Plot To Folder...")
        self.fileio_tab_output_select_directory_pushbutton.setFixedWidth(250)
        self.fileio_tab_output_select_directory_pushbutton.clicked.\
            connect(self.fileio_export_select_folder_directory)

        # Update export directory lineedit
        self.export_folder_path_selected_state.\
            connect(self.fileio_export_directory_update)

        self.fileio_tab_output_select_directory_lineedit = QLineEdit('')
        self.fileio_tab_output_select_directory_lineedit.setReadOnly(True)

    def fileio_export_select_folder_directory(self):
        """Generate a openfile dialogue for user to select
        a directory path that they wish to save their figure to.
        This method only handle selecting a path, but not determine
        whether the program will save it to the directory.
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        dialog_box_title = 'Select Output Directory to Export Graph'
        self.export_folder_path = QFileDialog.\
            getExistingDirectory(self, dialog_box_title)

        # save the folder path if successfully selected
        if (self.export_folder_path) and (self.export_folder_path != ''):
            print("Output Directory: ", self.export_folder_path)
            self.export_folder_path_selected_state.\
                emit("Output Directory Determined")

    @pyqtSlot(str)
    def fileio_export_directory_update(self, message):
        """This is the method that update the lineedit of the
        export file parameter when user select a folder to export
        the file to.

        Args:
            message (str): Check if there's changes to the export directory
        """
        if message == "Output Directory Determined":
            print("Output Directory Printed on Lineedit")
            self.fileio_tab_output_select_directory_lineedit.\
                setText(self.export_folder_path)

    def fileio_export_file_checkbox_figure_bool(self):
        """This method will tell whether outputting figure to a
        specific directory is valid. Only when the boolean here
        emit a true, that the program will allow the figure
        generated by this program to be saved.
        """
        if self.fileio_tab_export_checkbox.isChecked():
            if (self.fileio_tab_output_select_directory_lineedit.text() == ''):
                self.fileio_export_file_checkbox_uncheck()
                self.save_figs.emit(False)
            else:
                self.save_figs.emit(True)
        else:
            self.save_figs.emit(False)

    def fileio_export_file_checkbox_uncheck(self):
        """This method is called to uncheck the save output checkbox
        if user attempt to save output offline when the directory path
        is not given appropriately
        """
        print("Empty directory, cannot be saved offline")
        self.fileio_tab_export_checkbox.setCheckState(False)

    @pyqtSlot(bool)
    def save_fig_state(self, box_checked):
        """This method will be further added with detail
        on telling the neighborig tab whether to run
        the line that will save the figure offline.

        Args:
            box_checked (bool): To save or not save the figure
        """
        if box_checked:
            print("Figure will be saved")
        else:
            print("Figure will not be saved")

    def fileio_import_addwidget(self):
        """This method adds all the widgets for the import parameter
        section.
        """
        self.fileio_tab_import_configuration_layout.\
            addWidget(self.fileio_tab_import_configuration_pushbutton)
        self.fileio_tab_import_configuration_layout.\
            addWidget(self.fileio_tab_import_config_confirm_pushbutton)
        self.fileio_tab_import_configuration_layout.\
            addWidget(self.fileio_tab_import_config_label)

        # Add all import related widgets
        self.fileio_tab_import_layout_grid.\
            addWidget(self.fileio_tab_select_folder_pushbutton, 0, 0)
        self.fileio_tab_import_layout_grid.\
            addWidget(self.fileio_tab_select_folder_lineedit, 0, 1)
        self.fileio_tab_import_layout_grid.\
            addWidget(self.fileio_tab_import_selected_pushbutton, 1, 0)
        self.fileio_tab_import_layout_grid.\
            addWidget(self.fileio_tab_import_selected_label, 1, 1)
        self.fileio_tab_import_layout_grid.\
            addLayout(self.fileio_tab_import_configuration_layout, 2, 0,
                      Qt.AlignVCenter)
        self.fileio_tab_import_layout_grid.\
            addWidget(self.fileio_tab_import_selected_table, 2, 1)
        self.fileio_layout.addLayout(self.fileio_tab_import_layout_grid)
        self.fileio_layout.addStretch(20)

    def fileio_export_addwidget(self):
        """This section adds all widgets for the export parameter
        section.
        """
        # Add in all export related widgets
        self.fileio_tab_output_layout_grid.\
            addWidget(self.fileio_tab_export_checkbox, 0, 0)
        self.fileio_tab_output_layout_grid.\
            addWidget(self.fileio_tab_output_select_directory_pushbutton, 1, 0)
        self.fileio_tab_output_layout_grid.\
            addWidget(self.fileio_tab_output_select_directory_lineedit, 1, 1)
        self.fileio_layout.addLayout(self.fileio_tab_output_layout_grid)

    def select_an_csv_file_from_folder(self):
        for each_csv_selected in self.fileio_tab_import_selected_table.selectedIndexes():
            file_being_selected = self.fileio_tab_import_selected_fileModel.filePath(each_csv_selected)
            print(file_being_selected)
