import globals
import unit
import textRenderer
from time import sleep
import keyboard
import random
import colorama

prevPosX = []
prevPosY = []
curSelect = 0
curX = 0
curY = 0

def CenterCam(unit):
    globals.camOffsetX = max(0, min(unit.posX - (globals.camSizeX / 2), globals.mapSizeX - globals.camSizeX - 1))
    globals.camOffsetY = max(0, min(unit.posY - (globals.camSizeY / 2), globals.mapSizeX - globals.camSizeX - 1))

def StartGame():
    textRenderer.clearScreen()
    globals.defaultRenderer.Resize(globals.camSizeX * 4 + 1, globals.camSizeY * 2 + 1)

    curX = 0
    curY = 0
    curSelect = 0
    for i in globals.unitList:
        prevPosX.append(i.posX)
        prevPosY.append(i.posY)

    globals.gameState = 1
    globals.gameRunning = True
    
    GameLoop()

def GameLoop():
    lastKey = ""
    while (globals.gameRunning == True):
        if (not KeyHandler_Basic(lastKey)): # jeśli naciśnięty klawisz nie jest obsłużony przez podstawową funkcję
            if (globals.gameState == 2):  #ruch
                KeyHandler_Move(lastKey)
            elif (globals.gameState == 3):  #atak
                KeyHandler_Attack(lastKey)
            elif (globals.gameState == 4):  #ruch kamerą
                KeyHandler_Camera(lastKey)
        elif (not globals.gameRunning): # jeśli klawisz został obsłużony przez podstawową funkcję i spowodował on zakończenie gry
            break

        RenderMap()
        newKey = keyboard.read_key()
        if (newKey == lastKey):
            lastKey = ""
        else:
            lastKey = newKey
        sleep(0.016)

def EndTurn():
    for i in globals.unitList:
        i.moveRem = i.speed

        prevPosX.append(i.posX)
        prevPosY.append(i.posY)

def KeyHandler_Basic(key):
    global curX, curY, curSelect
    handled = False
    if (key == "esc"):
        if (globals.gameState != 1):
            globals.gameState = 1
        else:
            QuitPrompt()
        handled = True
        pass
    elif (key == "e"):
        EndTurn()
        globals.gameState = 1
        handled = True
        pass
    elif (key == "m"):
        curX = globals.unitList[curSelect].posX
        curY = globals.unitList[curSelect].posY
        globals.gameState = 2
        handled = True
        pass
    elif (key == "a"):
        globals.gameState = 3
        handled = True
        pass
    elif (key == "c"):
        globals.gameState = 4
        handled = True
        pass
    return handled

def KeyHandler_Move(key):
    handled = False
    global curX, curY, curSelect
    if (key == "up"):
        if (curY > 0):
            curY -= 1
        handled = True
    elif(key == "down"):
        if (curY < globals.mapSizeY):
            curY += 1
        handled = True
    elif(key == "right"):
        if (curX < globals.mapSizeX):
            curX += 1
        handled = True
    elif(key == "left"):
        if (curX > 0):
            curX -= 1
        handled = True
    elif (key == "1"):
        if (globals.unitList[0].health > 0):
            CenterCam(globals.unitList[0])
            curX = globals.unitList[0].posX
            curY = globals.unitList[0].posY
            curSelect = 0
        handled = True
        pass
    elif (key == "2"):
        if (globals.unitList[1].health > 0):
            CenterCam(globals.unitList[1])
            curX = globals.unitList[1].posX
            curY = globals.unitList[1].posY
            curSelect = 1
        handled = True
        pass
    elif (key == "3"):
        if (globals.unitList[2].health > 0):
            CenterCam(globals.unitList[2])
            curX = globals.unitList[2].posX
            curY = globals.unitList[2].posY
            curSelect = 2
        handled = True
        pass
    elif (key == "4"):
        if (globals.unitList[3].health > 0):
            CenterCam(globals.unitList[3])
            curX = globals.unitList[3].posX
            curY = globals.unitList[3].posY
            curSelect = 3
        handled = True
        pass
    elif (key == "5"):
        if (globals.unitList[4].health > 0):
            CenterCam(globals.unitList[4])
            curX = globals.unitList[4].posX
            curY = globals.unitList[4].posY
            curSelect = 4
        handled = True
    elif (key == "enter"):
        pass
    
    return handled

def KeyHandler_Attack(key):
    pass

def KeyHandler_Camera(key):
    handled = False
    if (key == "left"):
        if (globals.camOffsetX > 0):
            globals.camOffsetX -= 1
        handled = True
    elif (key == "up"):
        if (globals.camOffsetY > 0):
            globals.camOffsetY -= 1
        handled = True
    elif (key == "right"):
        if (globals.camOffsetX + globals.camSizeX < globals.mapSizeX):
            globals.camOffsetX += 1
        handled = True
    elif (key == "down"):
        if (globals.camOffsetY + globals.camSizeY < globals.mapSizeY):
            globals.camOffsetY += 1
        handled = True
    elif (key == "1"):
        if (globals.unitList[0].health > 0):
            CenterCam(globals.unitList[0])
        handled = True
        pass
    elif (key == "2"):
        if (globals.unitList[1].health > 0):
            CenterCam(globals.unitList[1])
        handled = True
        pass
    elif (key == "3"):
        if (globals.unitList[2].health > 0):
            CenterCam(globals.unitList[2])
        handled = True
        pass
    elif (key == "4"):
        if (globals.unitList[3].health > 0):
            CenterCam(globals.unitList[3])
        handled = True
        pass
    elif (key == "5"):
        if (globals.unitList[4].health > 0):
            CenterCam(globals.unitList[4])
        handled = True
    
    return handled

def QuitPrompt():
    textRenderer.clearScreen()
    print("\033[1m")
    print(textRenderer.GetColorCode(textRenderer.RED, textRenderer.RESETCOLOR), "Czy napewno chcesz wyjść? Naciśnij enter aby potwierdzić, inny klawisz spowoduje powrót do gry", sep="")
    sleep(0.25)
    key = keyboard.read_key()
    if (key == "enter"):
        globals.gameRunning = False
    textRenderer.clearScreen()

def RenderMap():
    global curX, curY, curSelect
    rightmost = globals.camSizeX * 4 + 1
    downmost = globals.camSizeY * 2 + 1

    globals.defaultRenderer.ClearBuffers()
    globals.defaultRenderer.FillColorAll(0)
    globals.defaultRenderer.GenGrid(0, 0, rightmost, downmost, 3, 1)
    if (globals.camOffsetY > 0):
        globals.defaultRenderer.FillChar("↑", 0, 0, rightmost, 0)

    if (globals.camOffsetX + globals.camSizeX < globals.mapSizeX):
        globals.defaultRenderer.FillChar("→", rightmost - 1, 0, rightmost - 1, downmost - 2)

    if (globals.camOffsetY + globals.camSizeY < globals.mapSizeY):
        globals.defaultRenderer.FillChar("↓", 0, downmost - 1, rightmost - 2, downmost - 1)

    if (globals.camOffsetX > 0):
        globals.defaultRenderer.FillChar("←", 0, 0, 0, downmost - 2)

    for i in globals.unitList:
        if (i.health == 0):
            continue
        elif (i.posX < globals.camOffsetX or i.posX >= globals.camOffsetX + globals.camSizeX):
            continue
        elif (i.posY < globals.camOffsetY or i.posY >= globals.camOffsetY + globals.camSizeY):
            continue

        globals.defaultRenderer.SetChar("O", (i.posX - globals.camOffsetX) * 4 + 2, (i.posY - globals.camOffsetY) * 2 + 1)
        if (i.ownerId == 0):
            globals.defaultRenderer.SetColor(textRenderer.GREEN << 4, (i.posX - globals.camOffsetX) * 4 + 2, (i.posY - globals.camOffsetY) * 2 + 1)
        else:
            globals.defaultRenderer.SetColor(textRenderer.RED << 4, (i.posX - globals.camOffsetX) * 4 + 2, (i.posY - globals.camOffsetY) * 2 + 1)

    if (globals.gameState == 2):
        renderCursorX = (curX - globals.camOffsetX) * 4 + 2
        renderCursorY = (curY - globals.camOffsetY) * 2 + 1
        globals.defaultRenderer.SetChar("V", renderCursorX, renderCursorY)
        globals.defaultRenderer.SetColor((textRenderer.GREEN << 4) + textRenderer.BLUE, renderCursorX, renderCursorY)

    globals.defaultRenderer.Overwrite()

