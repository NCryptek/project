import textRenderer

gameState = 0
gameRunning = False

defaultRenderer = textRenderer.TextRenderer(0, 0)
mapSizeX = 0
mapSizeY = 0
camOffsetX = 0
camOffsetY = 0
camSizeX = 10
camSizeY = 10

startUnitAmt = 0
playerAmt = 0

longestUnitName = 0

tileList = []
unitList = []
unitTemplates = []
startPositions = []

currentPlayer = 0
currentUnit = None

def Dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def GetPathFromTo(x1, y1, x2, y2):
    return

def GetUnitAt(x, y):
    if (x < 0 or x > mapSizeX - 1 or y < 0 or y > mapSizeY - 1):
        return None
    
    return tileList[y * mapSizeX + x]

def IsFreeFor(unit, x, y):
    if ((x < 0 or x >= mapSizeX) or (y < 0 or y >= mapSizeY)):
        return False

    dest = tileList[y * mapSizeX + x]
    if (dest != unit and dest != None):
        return False
    else:
        return True