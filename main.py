#!/usr/bin/python3 

### Client-server chat application built using PyQt ###
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton

# Create a GUI Application
app = QApplication([])

# Create our root window
window = QWidget() # imported

# Create a vertical layout and embed it in the root window
layout = QVBoxLayout() # is a class which is designed for lining  up widgets vertically
window.setLayout(layout)

# Create a text display
label = QLabel('Hello, Cyber')

# Make it visible
# label.show()

# Create a button
button = QPushButton('Click Me!')

# Add Widgets to the layout
layout.addWidget(label)
layout.addWidget(button)

window.show() # to display all the things that are inside the window including labels and buttons

# Enter the application's main loop 
# This method call doesn't end until the main window is closed
app.exec_() # runs the application

print("Application was closed") # Useful to display when the app is closed 
