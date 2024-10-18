#QMainWindow isn't very interesting at the moment. 
# We can fix that by adding some content.
# If you want to create a custom window, 
# the best approach is to subclass QMainWindow 
# and then include the setup for the window in the __init__ block.
# This allows the window behavior to be self contained.
# We can add our own subclass of QMainWindow — call it MainWindow to keep things simple.

import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication,QMainWindow,QPushButton

#Subclass QMainWIndow to customize apps main window
 #NEED TO REVISE OOPS
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button= QPushButton("Press Me!")
        
        #set the central widget of the window
        self.setCentralWidget(button)
        
app=QApplication(sys.argv)
window= MainWindow()
window.show()

app.exec()