import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow  

def main():
    app = QApplication(sys.argv)  # Create the application object
    main_window = MainWindow()    # Create an instance of your main window
    main_window.show()            # Show the main window
    sys.exit(app.exec_())         # Start the event loop

if __name__ == '__main__':
    main()
