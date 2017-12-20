import copy

gridWidth = 10
gridHeight = 10

def gridCreator(gridWidth, gridHeight):
    grid = []
    for k in range(0, gridHeight):
        gridLine = []
        for l in range(0, gridWidth):
            gridLine += [0]
        grid += [gridLine]

    return grid

def getCellCoords(actualGrid):
    bufferGrid = copy.deepcopy(actualGrid)
    OneList = []
    lineIndex = 0
    for l in bufferGrid:
        while l.count(1) > 0:
            OneList += [[lineIndex, l.index(1)]]
            l[l.index(1)] = 0
        lineIndex += 1
    return OneList

def countNeighbour(actualGrid, cellCoords):
    isLeftBorder = True if cellCoords[1] == 0 else False
    isRightBorder = True if cellCoords[1] == len(actualGrid[1])-1 else False
    isTopBorder = True if cellCoords[0] == 0 else False
    isBottomBorder = True if cellCoords[0] == len(actualGrid[0])-1 else False
    borderList = [isLeftBorder, isTopBorder, isRightBorder, isBottomBorder]
    borderCounter = borderList.count(True)

    if borderCounter == 2:
        print("Border = 2")
    elif borderCounter == 1:
        print("Border = 1")
    else:
        subGrid = actualGrid[cellCoords[0]-1:cellCoords[0]+2]
        BuffGrid = []
        for l in subGrid:
            BuffGrid += [l[cellCoords[1]-1:cellCoords[1]+2]]
        subGrid = BuffGrid
        subGrid[1][1] = 0
        displayGrid(subGrid)

def gridUpdater(actualGrid):
    cellCoords = getCellCoords(actualGrid)

    print(cellCoords)
    for cell in cellCoords:
        countNeighbour(actualGrid, cell)

def displayGrid(actualGrid):
    for l in actualGrid:
        print(l)
    print("")

#gameGrid[ligne][colonne]
gameGrid = gridCreator(gridWidth, gridHeight)

gameGrid[6][4] = 1
gameGrid[6][5] = 1
gameGrid[5][5] = 1
gameGrid[5][6] = 1
gameGrid[6][6] = 1
gameGrid[5][7] = 1

displayGrid(gameGrid)

print("")

gridUpdater(gameGrid)

