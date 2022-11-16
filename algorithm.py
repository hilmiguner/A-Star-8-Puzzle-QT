from state import State
from math import fabs

def heuristicFunc(tiles, goalTiles):
    count = 0
    for x1 in range(3):
        for y1 in range(3):
            goalStateRowIx = x1
            goalStateColumnIx = y1
            if goalTiles[goalStateRowIx][goalStateColumnIx] is None:
                continue
            for x2 in range(3):
                willBreak = False
                for y2 in range(3):
                    currentStateRowIx = x2
                    currentStateColumnIx = y2
                    if goalTiles[goalStateRowIx][goalStateColumnIx] == tiles[currentStateRowIx][currentStateColumnIx]:
                        count += fabs(goalStateRowIx-currentStateRowIx) + fabs(goalStateColumnIx - currentStateColumnIx)
                        willBreak = True
                        break
                if willBreak:
                    break
    return count


def createState(tiles, parentState, goalTiles):
    return State(tiles, parentState, heuristicFunc(tiles, goalTiles))

def arrangeFrontier(frontier):
    n = len(frontier)
    for i in range(n):
        for j in range(0, n - i - 1):
            if frontier[j].evaluation > frontier[j + 1].evaluation:
                frontier[j], frontier[j + 1] = frontier[j + 1], frontier[j]
    return frontier

def solution(state):
    solutionList = [state]
    temp = state
    while temp.parentState is not None:
        solutionList.insert(0, temp.parentState)
        temp = temp.parentState
    return solutionList

def A_Star(startState: State, goalStateTiles):
    frontier = []
    explored = []

    frontier.append(startState)


    while len(frontier) > 0:
        currentState = frontier.pop(0)

        if currentState.tiles == goalStateTiles:
            return solution(currentState)

        willAddExp = True
        for state in explored:
            if state.tiles == currentState.tiles:
                willAddExp = False
                break
        if willAddExp:
            explored.append(currentState)


        newStateTiles = currentState.expand()
        for tiles in newStateTiles:
            willAdd = True
            for exp in explored:
                if exp.tiles == tiles:
                    willAdd = False
                    break
            if willAdd:
                frontier.append(createState(tiles, currentState, goalStateTiles))
        frontier = arrangeFrontier(frontier)
    return -1
