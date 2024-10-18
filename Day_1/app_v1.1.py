import sys #for cmd argv
from PyQt6.QtWidgets import QApplication, QPushButton 
#this shows any widget can be imported as window
#in last ver1.0 it was Qwidget now it's push button
app=QApplication(sys.argv)

window=QPushButton("Push Here")
window.show()

app.exec()

#next is the main window cuz app consists of multiple nested windows