'''
This script is written to add the widgets
for the graph analysis tab.

Author: Aiden Chen
Date: 11-28-2019
'''
# standard library

# third party libraries
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QCheckBox, QComboBox
from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton, QSpinBox
from PyQt5.QtWidgets import QFileDialog, QFileSystemModel, QListView
from PyQt5.QtGui import QFont

# local file libraries


class GraphAnalysisTab(QWidget):
    '''This class houses all the set widgets used for the graph analysis tab
    '''

    # Class attribute

    def __init__(self):
        super().__init__()
        # instance variables

        # define outer structure of this tab
        self.graph_analysis_layout = QVBoxLayout()

        # graph analysis tab label
        self.graph_analysis_tab_title_label = QLabel()
        self.graph_analysis_tab_title_label.setFont(QFont('Arial', 10))
        self.graph_analysis_tab_title_label.\
            setText('<b>Graph Analysis Tab</b>')
        self.graph_analysis_layout.\
            addWidget(self.graph_analysis_tab_title_label)

        # define a larger grid structure below the header
        self.graph_analysis_parameters_grid = QGridLayout()

        # define the left side to be smaller grid
        self.graph_analysis_parameter_left_grid = QGridLayout()
        
        # TODO: Add input field and labels on the left side of the grid
        self.graph_analysis_trigger_type_label = QLabel("Trigger Type: ")
        self.graph_analysis_trigger_type_combobox = QComboBox()
        trigger_items = ['Free Run', 'Positive Edge']
        self.graph_analysis_trigger_type_combobox.addItems(trigger_items)

        self.graph_analysis_total_analysis_time_label = QLabel()
        self.graph_analysis_total_analysis_time_label.\
            setText('Total Analysis Time: ')
        self.graph_analysis_total_analysis_time_spinbox = QSpinBox()

        self.graph_analysis_time_delay_to_analyze_label = QLabel()
        self.graph_analysis_time_delay_to_analyze_label.\
            setText('Time Delay Before Analysis: ')
        self.graph_analysis_time_delay_to_analyze_spinbox = QSpinBox()

        self.graph_analysis_pmin_label = QLabel('Pmin: ')
        self.graph_analysis_pmin_spinbox = QSpinBox()

        self.graph_analysis_pmax_label = QLabel('Pmax: ')
        self.graph_analysis_pmax_spinbox = QSpinBox()

        # define the right side to be vertical box
        self.graph_analysis_parameter_right_grid = QVBoxLayout()

        # TODO: Modularize it
        self.graph_analysis_left_grid_addwidget()   # add left grid to the larger grid layout


        # TODO: Add 1 generate plot button on the right side of the grid
        # TODO: Modularize it

        # add the outer grid to the application
        self.graph_analysis_layout.\
            addLayout(self.graph_analysis_parameters_grid)

        self.setLayout(self.graph_analysis_layout)

    def graph_analysis_left_grid_addwidget(self):
        '''This method adds all the widgets for the parameter left grid
        section.
        '''
        # the left-grid variable: self.graph_analysis_parameter_left_grid

        # the trigger type widget
        self.graph_analysis_parameter_left_grid.\
            addWidget(self.graph_analysis_trigger_type_label, 0, 0)
        self.graph_analysis_parameter_left_grid.\
            addWidget(self.graph_analysis_trigger_type_combobox, 0, 1)
        self.graph_analysis_parameter_left_grid.\
            addWidget(self.graph_analysis_total_analysis_time_label, 1, 0)
        self.graph_analysis_parameter_left_grid.\
            addWidget(self.graph_analysis_total_analysis_time_spinbox, 1, 1)
        self.graph_analysis_parameter_left_grid.\
            addWidget(self.graph_analysis_time_delay_to_analyze_label, 2, 0)
        self.graph_analysis_parameter_left_grid.\
            addWidget(self.graph_analysis_time_delay_to_analyze_spinbox, 2, 1)
        self.graph_analysis_parameter_left_grid.\
            addWidget(self.graph_analysis_pmin_label, 3, 0)
        self.graph_analysis_parameter_left_grid.\
            addWidget(self.graph_analysis_pmin_spinbox, 3, 1)
        self.graph_analysis_parameter_left_grid.\
            addWidget(self.graph_analysis_pmax_label, 4, 0)
        self.graph_analysis_parameter_left_grid.\
            addWidget(self.graph_analysis_pmax_label, 4, 1)
        self.graph_analysis_parameters_grid.\
            addLayout(self.graph_analysis_parameter_left_grid, 0, 0)



