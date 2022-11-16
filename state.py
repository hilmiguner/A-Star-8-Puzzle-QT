from copy import deepcopy

class State:
    def __init__(self, tiles, parentState, heuristic):
        self.tiles = tiles

        # -------------FINDING POSITION OF BLANK TILE-------------
        self.blankPos = None
        for i in range(3):
            willBreak = False
            for j in range(3):
                if self.tiles[i][j] is None:
                    self.blankPos = (i, j)
                    willBreak = True
                    break
            if willBreak:
                break
        # --------------------------------------------------------

        # -------------PARENT STATE-------------
        self.parentState = parentState
        # --------------------------------------

        # -------------CALCULATING FUNCTIONS-------------
        self.cost = self.costFunc()
        self.heuristic = heuristic
        self.evaluation = self.cost + self.heuristic
        # -----------------------------------------------

    def costFunc(self):
        if self.parentState is not None:
            return self.parentState.cost + 1
        else:
            return 0

    def expand(self):
        checkLeft = [(0, 0), (1, 0), (2, 0)]
        checkUp = [(0, 0), (0, 1), (0, 2)]
        checkRight = [(0, 2), (1, 2), (2, 2)]
        checkDown = [(2, 0), (2, 1), (2, 2)]

        checkDict = {"left": True, "up": True, "right": True, "down": True}

        if self.blankPos in checkLeft:
            checkDict["left"] = False
        if self.blankPos in checkUp:
            checkDict["up"] = False
        if self.blankPos in checkRight:
            checkDict["right"] = False
        if self.blankPos in checkDown:
            checkDict["down"] = False

        rowIx = self.blankPos[0]
        columnIx = self.blankPos[1]

        newStateTiles = []

        for key in checkDict:
            newTiles = deepcopy(self.tiles)
            if key == "left" and checkDict[key] is True:
                newTiles[rowIx][columnIx], newTiles[rowIx][columnIx-1] = newTiles[rowIx][columnIx-1], newTiles[rowIx][columnIx]
                newStateTiles.append(newTiles)
            elif key == "up" and checkDict[key] is True:
                newTiles[rowIx][columnIx], newTiles[rowIx-1][columnIx] = newTiles[rowIx-1][columnIx], newTiles[rowIx][columnIx]
                newStateTiles.append(newTiles)
            elif key == "right" and checkDict[key] is True:
                newTiles[rowIx][columnIx], newTiles[rowIx][columnIx+1] = newTiles[rowIx][columnIx+1], newTiles[rowIx][columnIx]
                newStateTiles.append(newTiles)
            elif key == "down" and checkDict[key] is True:
                newTiles[rowIx][columnIx], newTiles[rowIx+1][columnIx] = newTiles[rowIx+1][columnIx], newTiles[rowIx][columnIx]
                newStateTiles.append(newTiles)

        return newStateTiles
