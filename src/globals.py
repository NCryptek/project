mapSizeX = 0
mapSizeY = 0

startUnitAmt = 0
playerAmt = 0

tileList = []
unitList = []

currentPlayer = 0
currentUnit = None

def Dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def GetPathFromTo(x1, y1, x2, y2):
    return

def IsFreeFor(unit, x, y):
    if ((x < 0 or x >= mapSizeX) or (y < 0 or y >= mapSizeY)):
        return False

    dest = tileList[y * mapSizeX + x]
    if (dest != unit and dest != None):
        return False
    else:
        return True