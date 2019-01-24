from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton

class ChatUI(): # creation of a class 
    """This class encapsulates out application""" 

    def __init__(self):

        # counter for number of clicks to be stored 
        self.button_clicks = 0

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
        button = QPushButton('Click Me!') # button was defined here

        def on_button_clicked(): # will count the button clicks
            global button_clicks # need a global variable so it is defined 
            button_clicks += 1 # increments clicks by 1

            label.setText("Button was clicked " + str(button_clicks) + " times")

        button.clicked.connect(on_button_clicked) # passed in function name
    
    


        # Add Widgets to the layout
        layout.addWidget(label)
        layout.addWidget(button)

        window.show() # to display all the things that are inside the window including labels and buttons

    
        # Enter the application's main loop 
        # This method call doesn't end until the main window is closed
        app.exec_() # runs the application

        print("Application was closed") # Useful to display when the app is closed 
