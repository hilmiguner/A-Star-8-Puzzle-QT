import sys

from PyQt5 import QtWidgets
from interfaces_py.mainWindow import Ui_MainWindow
from PyQt5.QtCore import Qt

from algorithm import A_Star, createState

class myWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.uiManager = Ui_MainWindow()
        self.uiManager.setupUi(self)

        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()

        startStateTiles = [[1, 7, 6], [8, 3, 4], [5, 2, None]]
        goalStateTiles = [[1, 2, 3], [4, 5, 6], [7, 8, None]]
        startState = createState(tiles=startStateTiles, parentState=None, goalTiles=goalStateTiles)
        self.result = A_Star(startState=startState, goalStateTiles=goalStateTiles)
        for ix, state in enumerate(self.result):
            stateWidget = QtWidgets.QWidget()
            gridLayout = QtWidgets.QGridLayout()
            for i in range(3):
                for j in range(3):
                    label = QtWidgets.QLabel()
                    label.setText(str(state.tiles[i][j]))
                    label.setAlignment(Qt.AlignCenter)
                    label.setFixedSize(30, 30)
                    label.setStyleSheet("""border:1px solid red;""")

                    labelCount = QtWidgets.QLabel()
                    labelCount.setText(f"{ix}. step")

                    gridLayout.addWidget(label, i, j)
                    gridLayout.addWidget(labelCount, 3, 1)
            stateWidget.setLayout(gridLayout)
            layout.addWidget(stateWidget)

        widget.setLayout(layout)
        self.uiManager.scrollArea.setWidget(widget)

app = QtWidgets.QApplication(sys.argv)
window = myWindow()
window.show()
app.exec()