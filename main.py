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

        self.uiManager.btn_Start.clicked.connect(self.action_btn_StartClicked)

    def action_btn_StartClicked(self):
        self.uiManager.btn_Start.setEnabled(False)
        self.uiManager.gridLayout.setEnabled(False)
        self.uiManager.gridLayout_2.setEnabled(False)

        verticalLayout = QtWidgets.QVBoxLayout()
        horizontalLayout = QtWidgets.QHBoxLayout()
        widget = QtWidgets.QWidget()

        startStateTiles = [[], [], []]
        goalStateTiles = [[], [], []]

        for x in range(3):
            for y in range(3):
                text = self.uiManager.gridLayout.itemAtPosition(x, y).widget().currentText()
                if text == "None":
                    text = None
                else:
                    text = int(text)
                startStateTiles[x].append(text)

        for x in range(3):
            for y in range(3):
                text = self.uiManager.gridLayout_2.itemAtPosition(x, y).widget().currentText()
                if text == "None":
                    text = None
                else:
                    text = int(text)
                goalStateTiles[x].append(text)

        startState = createState(tiles=startStateTiles, parentState=None, goalTiles=goalStateTiles)
        result, createdNode, maxDepth = A_Star(startState=startState, goalStateTiles=goalStateTiles)
        for ix, state in enumerate(result):
            if ix % 5 == 0:
                horizontalLayout = QtWidgets.QHBoxLayout()
            stateWidget = QtWidgets.QWidget()
            stateWidget.setFixedSize(120, 140)
            gridLayout = QtWidgets.QGridLayout()
            for i in range(3):
                for j in range(3):
                    label = QtWidgets.QLabel()
                    label.setText(str(state.tiles[i][j]))
                    label.setAlignment(Qt.AlignCenter)
                    label.setFixedSize(30, 30)
                    label.setStyleSheet("""border:1px solid red;""")

                    labelCount = QtWidgets.QLabel()
                    labelCount.setAlignment(Qt.AlignCenter)
                    labelCount.setFixedSize(50, 30)
                    labelCount.setText(f"{ix}. step")

                    gridLayout.addWidget(label, i, j)
                    gridLayout.addWidget(labelCount, 3, 1)

            stateWidget.setLayout(gridLayout)
            horizontalLayout.addWidget(stateWidget)
            if ix % 5 == 0:
                temp = QtWidgets.QWidget()
                temp.setLayout(horizontalLayout)
                verticalLayout.addWidget(temp)

        widget.setLayout(verticalLayout)
        self.uiManager.scrollArea.setWidget(widget)

        self.uiManager.label.setText(f"Total created node: {createdNode}")
        self.uiManager.label_2.setText(f"Maximum depth: {maxDepth}")

        self.uiManager.btn_Start.setEnabled(True)
        self.uiManager.gridLayout.setEnabled(True)
        self.uiManager.gridLayout_2.setEnabled(True)

app = QtWidgets.QApplication(sys.argv)
window = myWindow()
window.show()
app.exec()