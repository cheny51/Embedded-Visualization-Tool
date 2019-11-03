'''
This script is written to
create the tabs inside the main application
window.

Author: Aiden Chen
'''
from PyQt5.QtWidgets import QTabWidget, QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import pyqtSlot


class TabbedGui(QWidget):
    '''This class is written to configure
    the 2 tabs in the QMainWindow
    '''
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabbed_gui_widget = QTabWidget()
        self.file_io_tab = QWidget()
        self.graph_analysis_tab = QWidget()
        self.tabbed_gui_widget.resize(300, 200)

        # add tabs
        self.tabbed_gui_widget.addTab(self.file_io_tab, "File IO")
        self.tabbed_gui_widget.addTab(self.graph_analysis_tab, "Graph Analysis")

        # add tabs to widget
        self.layout.addWidget(self.tabbed_gui_widget)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(),
                  currentQTableWidgetItem.text())
