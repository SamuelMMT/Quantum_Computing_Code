import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import pyqtgraph.opengl as gl
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Quantum Simulator')
        self.setGeometry(100, 100, 800, 600)

        # Create a GL View widget to display data
        self.glWidget = gl.GLViewWidget()
        self.setCentralWidget(self.glWidget)

        # Create a sphere (Bloch sphere representation)
        sphere = gl.MeshData.sphere(rows=10, cols=20)
        sphereItem = gl.GLMeshItem(meshdata=sphere, smooth=True, shader='shaded', color=(1, 1, 1, 0.3), glOptions='translucent')
        self.glWidget.addItem(sphereItem)

        # Initialize the state vector arrow
        self.stateVector = gl.GLLinePlotItem(pos=np.array([[0,0,0], [1,0,0]]), color=(1,0,0,1), width=2)
        self.glWidget.addItem(self.stateVector)

    def updateState(self, x, y, z):
        # Update the position of the state vector
        self.stateVector.setData(pos=np.array([[0,0,0], [x,y,z]]))


def main():
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
