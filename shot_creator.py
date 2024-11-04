from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QDialog, QPushButton, QHBoxLayout, QTextEdit, QCheckBox, QScrollArea, QGroupBox, QTreeWidget, QTreeWidgetItem, QProgressDialog, QMenu, QAction, QMessageBox, QFileDialog
)
from PyQt5.QtCore import Qt, QByteArray, QTimer, QFileInfo, QUrl
from PyQt5.QtGui import QPixmap, QTextDocument
from PyQt5.QtPrintSupport import QPrinter
import traceback

import os
import shutil
import toml


"""
Introduction:
The following code defines a PyQt5 QWidget-based class named `SHOT_CREATOR`. This class is designed as a template to retrieve data from ShotGrid and handle specific actions when data is received. 
You are tasked with creating a structure based on a dictionary that includes the keys 'code' and 'sg_sequence'. 
Example: {'code' : 'DEV_0010A_0010', 'sg_sequence' : {'type': 'Sequence', 'code' : '0010A'}}

The structure should follow a specific pattern using the given example, such as "040_SOURCES/{shot}/010_PLATES". 
If the shot contains sequence it contain a sequence folder.
Examples:
040_SOURCES/0010A/DEV_0010A_0010/010_PLATES  # if sequence exists and is not Nonetype
040_SOURCES/DEV_0010A_0010/010_PLATES  # if sequence does not exist / or is Nonetype

Your Task:
- Use the provided dictionary data to build a directory structure.
- Use the `code` and `sg_sequence` values from the dictionary to populate the structure.
- Use the structure from provided CONF file.

Below are detailed comments explaining the various parts of the code.
"""

'''
Notes:
CWD (Current Working Directory) points to main NL Hub directory. Please note that loading files will work under ./plugins/<plugin_folder>/<file>
'''

class SHOT_CREATOR(QWidget):
    NAME = '_SHOT CREATOR' # NAME OF APP VISIBLE
    ICON = '' # FULL PATH to ICON or RELATIVE To main folder (libs, icons). If left blank or path is unconstructable, sets default icon.
    SHOW_SHOTGRID = False #Make it false if you don't want the shotgrid Group window.
    PERMISSION = []
    HIDDEN = True
    ENDPOINT = '/shot_creator'

    def __init__(self, main, logger):
        super().__init__()
        '''
        Use self.main for shotgun and other app references
        Use self.logger to log information.

        '''
        self.main = main
        self.logger = logger
    
    def recieve(self, data):

        def retrieve_data():
            data = self._retrieve_data(data.get('data'))

            '''
            Space to place your code for Structure generation.            
            '''

            progress_dialog.close()





        self.logger.info(data)
        #self.logger.debug(data)

        if data['endpoint'] == self.ENDPOINT:
            progress_dialog = QProgressDialog("Creating Shots...", "Cancel", 0, 0, self)
            progress_dialog.setWindowModality(Qt.WindowModal)
            progress_dialog.setWindowFlags(progress_dialog.windowFlags() | Qt.WindowStaysOnTopHint)
            
            progress_dialog.show()
            QTimer.singleShot(2000, retrieve_data)
            
    

    def _retrieve_data(self, data):
        '''
        Retrieve data from Shotgun    
        
        '''

        if type(data.get('selected_ids')) == list:
            data['selected_ids'] = data['selected_ids'][0]

        if ',' in data['selected_ids']:
            ids = [int(id) for id in data['selected_ids'].split(',')]
        else:
            ids = [int(data['selected_ids'])]
        
        shots = self.main.sg.find('Shot', [['id', 'in', ids]], ['code', 'sg_sequence'])

        self.logger.info(shots)

        return shots
        
        
    
    def cleanup(self, directory):
        '''
        Cleanup code for if the temporary directory existed.
        '''
        pass