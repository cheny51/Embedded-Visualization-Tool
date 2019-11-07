'''
The purpose of this script is to house
functions that is not for button or for labels,
for example, the openfile dialogue box.

Created: 11/6/2019
Author: Aiden Chen
'''
import sys
from PyQt5.QtWidgets import QFileDialog, QLineEdit


def fileio_tab_select_folder_pushbutton_clicked(self):
    '''This function calls when select folder pushbutton
    is being pressed. It will open up a import dialog,
    and asks user to select a folder to import.
    '''
    fileio_import_files_from_folder_dialog(self)


def fileio_import_files_from_folder_dialog(self):
    '''This function opens a file dialogue, and it will
    ask user to select a folder to open, and if the folder
    is selected and opened, it search for the .csv just
    in that folder.
    '''
    # configure the input file dialog
    folder_select_dialog_box = QFileDialog.Options()
    folder_select_dialog_box |= QFileDialog.DontUseNativeDialog
    dialog_box_title = 'Select Directory with .csv data files'
    folder_path = QFileDialog.getExistingDirectory(self,
                                                   dialog_box_title)
    print(folder_path)
    # save the folder import path
    # self.fileio_tab_select_file_lineedit.setText(folder_path)
