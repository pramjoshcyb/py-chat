[1mdiff --git a/main.py b/main.py[m
[1mold mode 100644[m
[1mnew mode 100755[m
[1mindex e69de29..574c42d[m
[1m--- a/main.py[m
[1m+++ b/main.py[m
[36m@@ -0,0 +1,35 @@[m
[32m+[m[32m#!/usr/bin/python3[m[41m [m
[32m+[m
[32m+[m[32m### Client-server chat application built using PyQt ###[m
[32m+[m[32mfrom PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton[m
[32m+[m
[32m+[m[32m# Create a GUI Application[m
[32m+[m[32mapp = QApplication([])[m
[32m+[m
[32m+[m[32m# Create our root window[m
[32m+[m[32mwindow = QWidget() # imported[m
[32m+[m
[32m+[m[32m# Create a vertical layout and embed it in the root window[m
[32m+[m[32mlayout = QVBoxLayout() # is a class which is designed for lining  up widgets vertically[m
[32m+[m[32mwindow.setLayout(layout)[m
[32m+[m
[32m+[m[32m# Create a text display[m
[32m+[m[32mlabel = QLabel('Hello, Cyber')[m
[32m+[m
[32m+[m[32m# Make it visible[m
[32m+[m[32m# label.show()[m
[32m+[m
[32m+[m[32m# Create a button[m
[32m+[m[32mbutton = QPushButton('Click Me!')[m
[32m+[m
[32m+[m[32m# Add Widgets to the layout[m
[32m+[m[32mlayout.addWidget(label)[m
[32m+[m[32mlayout.addWidget(button)[m
[32m+[m
[32m+[m[32mwindow.show() # to display all the things that are inside the window including labels and buttons[m
[32m+[m
[32m+[m[32m# Enter the application's main loop[m[41m [m
[32m+[m[32m# This method call doesn't end until the main window is closed[m
[32m+[m[32mapp.exec_() # runs the application[m
[32m+[m
[32m+[m[32mprint("Application was closed") # Useful to display when the app is closed[m[41m [m
