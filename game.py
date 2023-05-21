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
        elif (not globals.gameRunning):
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
    pass

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

    globals.defaultRenderer.Overwrite()

