#version_1.0
from PyQt6.QtWidgets import QApplication, QWidget

#Only needed for access to command line arguments
import sys

#We need one (and only one) QApplication instance per application
#Pass in sys.argv to allow cmd line arguments for our app.
#If we know we wont use command line args QApplication([]) works too.
app= QApplication(sys.argv)

#The core of every Qt Applications is the QApplication class.
# Every application needs one — and only one — QApplication object to function

#sys.arg, which is Python list containing the command line arguments passed to the application.

#Create a Qt widget, which will be our window.
window= QWidget()
window.show() #IMP!!!! windows are hidden by default

#You can remove the .show() and run the app, but you'll have no way to quit it!

#start the event loop.
app.exec()


#The QApplication class - QApplication holds the Qt event loop 
# - One QApplication instance required -
# our application sits waiting in the event loop until an action is taken 
# - There is only one event loop running at any time
#app won't reach here untill we exit the event
#Loop has stopped    
