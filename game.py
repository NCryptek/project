import globals
import unit
import textRenderer
from time import sleep
import keyboard
import random
import colorama


def StartGame():
    textRenderer.clearScreen()
    globals.defaultRenderer.Resize(globals.camSizeX * 4 + 1, globals.camSizeY * 2 + 1)
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
        lastKey = keyboard.read_key()
        sleep(0.1)

def EnemyTurn():
    pass

def KeyHandler_Basic(key):
    handled = False
    if (key == "esc"):
        if (globals.gameState != 1):
            globals.gameState = 1
        else:
            QuitPrompt()
        handled = True
        pass
    elif (key == "e"):
        EnemyTurn()
        handled = True
        pass
    elif (key == "m"):
        globals.gameState = 2
        handled = True
        pass
    elif (key == "a"):
        handled = True
        pass
    elif (key == "c"):
        handled = True
        pass
    elif (key == "1"):
        handled = True
        pass
    elif (key == "2"):
        handled = True
        pass
    elif (key == "3"):
        handled = True
        pass
    elif (key == "4"):
        handled = True
        pass
    elif (key == "5"):
        handled = True
        pass

    return handled

def KeyHandler_Move(key):
    handled = False
    if (key == "esc"):
        pass
    elif(key == "up"):
        if (globals.CursorY < globals.mapSizeY):
            globals.CursorY +=1
            handled = True
    elif(key == "down"):
        if (globals.CursorY > 0):
            globals.CursorY-=1
            handled = True
    elif(key == "right"):
        if (globals.CursorX < globals.mapSizeX):
            globals.CursorX +=1
            handled = True
    elif(key == "left"):
        if (globals.CursorX > 0):
            globals.CursorX -=1
            handled = True
    print("ty")
    print(globals.CursorX, globals.CursorY)
    print(key)
    return handled
    

def KeyHandler_Attack(key):
    pass

def KeyHandler_Camera(key):
    pass

def QuitPrompt():
    textRenderer.clearScreen()
    print("\033[1m")
    print(textRenderer.GetColorCode(textRenderer.RED, textRenderer.RESETCOLOR), "Czy napewno chcesz wyjść? Naciśnij enter aby potwierdzić, inny klawisz spowoduje powrót do gry", sep="")
    key = keyboard.read_key()
    if (key == "enter"):
        globals.gameRunning = False
    textRenderer.clearScreen()

def RenderMap():
    globals.defaultRenderer.GenGrid(0, 0, globals.camSizeX * 4 + 1, globals.camSizeY * 2 + 1, 3, 1)
    for i in globals.unitList:
        if (i.health == 0):
            continue
        elif (i.posX < globals.camOffsetX or i.posX >= globals.camOffsetX + globals.camSizeX):
            continue
        elif (i.posY < globals.camOffsetY or i.posY >= globals.camOffsetY + globals.camSizeY):
            continue

        globals.defaultRenderer.SetChar("O", (i.posX - globals.camOffsetY) * 4 + 2, (i.posY - globals.camOffsetY) * 2 + 1)
        globals.defaultRenderer.SetColor(textRenderer.GREEN << 4, (i.posX - globals.camOffsetY) * 4 + 2, (i.posY - globals.camOffsetY) * 2 + 1)
        

    globals.defaultRenderer.Overwrite()

