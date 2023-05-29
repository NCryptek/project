import globals
import unit
from game import StartGame
import keyboard
import random
from time import sleep
import textRenderer

def setup():
    print("\033[1m")
    MapSize()
    PlayerCount()
    BuildUnits()
    StartGame()
#enddef setup

def MapSize():
    value = True
    while value:
        textRenderer.clearScreen()
        print("Proszę nie podawaj zbyt dużych wartości.")
        print("Podaj wielkość mapy OSOBNO ORAZ KOLEJNO poziomo i pionowo")
        mapSizeX = input()
        mapSizeY = input()
        try:
            globals.mapSizeX = int(mapSizeX)
            globals.mapSizeY = int(mapSizeY)
        except:
            continue
        value = False
    
    globals.tileList = [None] * (globals.mapSizeX * globals.mapSizeY)

    globals.startPositions.append([1, 1])
    globals.startPositions.append([3, 1]) # 1 2
    globals.startPositions.append([2, 2]) #  3
    globals.startPositions.append([1, 3]) # 4 5
    globals.startPositions.append([3, 3])

    globals.startPositions.append([globals.mapSizeX - 2, globals.mapSizeY - 2])
    globals.startPositions.append([globals.mapSizeX - 4, globals.mapSizeY - 2])
    globals.startPositions.append([globals.mapSizeX - 3, globals.mapSizeY - 3])
    globals.startPositions.append([globals.mapSizeX - 2, globals.mapSizeY - 4])
    globals.startPositions.append([globals.mapSizeX - 4, globals.mapSizeY - 4])

def PlayerCount():
    value = True
    while value:
        textRenderer.clearScreen()
        print("Podaj ilość jednostek na gracza (1-5)")
        #playerCount = #input()
        armySize = input()
        try:
            globals.playerAmt = 2 #int(playerCount)
            globals.startUnitAmt = int(armySize)
        except:
            continue
        #if (playerCount<1 or playerCount > 4):
        #    continue
        if (int(armySize)<1 or int(armySize)>5):
            continue
        value = False 

def BuildUnits():
    #wymagana jest najdłuższa możliwa nazwa jednostki aby móc poprawnie stworzyć bufor,
    #nie może być poniżej 12 żeby poprawnie wyświetlać statystyki
    longestName = 12
    for i in globals.unitTemplates:
        if (longestName < len(i.displayName)):
            longestName = len(i.displayName)

    #wyczyszczenie ekranu i ustawienie rozmiaru bufora
    textRenderer.resetCursorPos()
    globals.defaultRenderer.ClearScreen()
    globals.defaultRenderer.Resize(2 * longestName + 11, 15)
    
    #inicjalizacja stałego tekstu
    #poszczególne jednostki
    for i in range(globals.startUnitAmt):
        globals.defaultRenderer.InsertText(f"  U{i + 1}: ", 0, i)

    #poszczególne typy jednostek 
    #for i in range(len(globals.unitTemplates)):
    #    globals.defaultRenderer.InsertText(f"     {globals.unitTemplates[i].displayName}", longestName + 6, i)
    #globals.defaultRenderer.FillColor(textRenderer.BLACK << 4, longestName + 6, 0, 2 * longestName + 11, len(globals.unitTemplates))

    globals.defaultRenderer.InsertText("  Zatwierdź", 0, 7)

    #statystyki obecnie wyświetlanej jednostki
    globals.defaultRenderer.InsertTextSpecial("Życie:\nAtak:\nZasięg:\nRuchy:\nTyp broni:\nTyp pancerza:", 2, 9, 18, 14)

    #wypisanie do testu!
    #globals.defaultRenderer.Print()

    #wstrzymanie do testu!
    #input()

    selects = []
    curOption = 0
    changeTo = -1
    lastKey = ""
    for i in range(globals.startUnitAmt):
        selects.append(i)

    while True:
        if (changeTo == -1): #wybieranie jednostki do zmiany
            #obsługa klawiszy
            if (lastKey == "up"): #strzałka w górę
                curOption -= 1
            elif (lastKey == "down"): #strzałka w dół
                curOption += 1
            elif (lastKey == "enter"):
                if (curOption == globals.startUnitAmt):
                    globals.defaultRenderer.ClearBuffers()
                    break
                else:
                    globals.defaultRenderer.FillColor(textRenderer.YELLOW << 4, 6, curOption, 6 + longestName, curOption)
                    changeTo = selects[curOption]
                    for i in range(len(globals.unitTemplates)):
                        globals.defaultRenderer.InsertText(f"     {globals.unitTemplates[i].displayName}", longestName + 6, i)
                    globals.defaultRenderer.InsertText("  ----->  ", 18, 9)
                    globals.defaultRenderer.InsertTextSpecial("Życie:\nAtak:\nZasięg:\nRuchy:\nTyp broni:\nTyp pancerza:", 28, 9, 44, 14)
            
            #naprawienie wybranej opcji
            if (curOption < 0):
                curOption = globals.startUnitAmt
            elif (curOption > globals.startUnitAmt):
                curOption = 0
            
            #render
            globals.defaultRenderer.FillChar(" ", 0, 0, 1, 7)
            if (curOption == globals.startUnitAmt):
                globals.defaultRenderer.FillChar(">", 0, 7, 0, 7)
            else:
                globals.defaultRenderer.FillChar(">", 0, curOption, 0, curOption)

            globals.defaultRenderer.FillChar(" ", 6, 0, 6 + longestName, globals.startUnitAmt)
            for i in range(globals.startUnitAmt):
                globals.defaultRenderer.InsertText(globals.unitTemplates[selects[i]].displayName, 6, i)
            
            #statystyki bieżącej jednostki
            if (curOption < globals.startUnitAmt):
                templateRef = globals.unitTemplates[selects[curOption]]
                globals.defaultRenderer.InsertTextSpecial(f"{templateRef.maxHealth}\n{templateRef.damage}\n{templateRef.range}\n{templateRef.speed}\n{unit.warheads[templateRef.damageType]}\n{unit.armors[templateRef.armorType]}", 16, 9, 18, 14)

        else: #wybieranie typu jednostki na który zmienić
            #obsługa klawiszy
            if (lastKey == "up"): #strzałka w górę
                changeTo -= 1
            elif (lastKey == "down"): #strzałka w dół
                changeTo += 1
            elif (lastKey == "enter"):
                globals.defaultRenderer.FillColor(textRenderer.RESETCOLOR << 4, 6, curOption, 6 + longestName, curOption)
                globals.defaultRenderer.FillChar(" ", longestName + 6, 0, 2 * longestName + 11, len(globals.unitTemplates))
                globals.defaultRenderer.FillChar(" ", 18, 9, 44, 14)
                selects[curOption] = changeTo
                changeTo = -1
            
            #naprawienie wybranej opcji
            if (curOption < 0):
                changeTo = len(globals.unitTemplates) - 1
            elif (curOption >= len(globals.unitTemplates)):
                changeTo = 0
            #render
            templateRef = globals.unitTemplates[changeTo]
            if (changeTo != -1): #w przeciwnym razie wkleja tekst w miejscu gdzie go nie powinno być po wybraniu typu
                globals.defaultRenderer.FillChar(" ", 6 + longestName, 0, 10 + longestName, len(globals.unitTemplates))
                globals.defaultRenderer.InsertTextSpecial(f"{templateRef.maxHealth}\n{templateRef.damage}\n{templateRef.range}\n{templateRef.speed}\n{unit.warheads[templateRef.damageType]}\n{unit.armors[templateRef.armorType]}", 42, 9, 44, 14)
                globals.defaultRenderer.InsertText("-->", 7 + longestName, changeTo)
        #endif
        globals.defaultRenderer.Overwrite()
        if (lastKey != "enter"):
            lastKey = keyboard.read_key()
        else:
            lastKey = ""
        sleep(0.1)
    #endwhile

    for i in selects:
        globals.unitList.append(unit.Unit(globals.startPositions[i][0], globals.startPositions[i][1], globals.unitTemplates[i], 0))

    for i in range(globals.startUnitAmt):
        globals.unitList.append(unit.Unit(globals.startPositions[5 + i][0], globals.startPositions[5 + i][1], globals.unitTemplates[random.randint(0, len(globals.unitTemplates) - 1)], 1))
#enddef BuildUnits

"""
def printWhite(data):
    print(Fore.WHITE,data,end="",sep="")

def printRed(data):
    print(Fore.RED,data,end="",sep="")

def printGreen(data):
    print(Fore.GREEN,data,end="",sep="")

def printScreen():
    corners = {
        "upperLeft":     "┌",    
        "upperRight":    "┐",    
        "mediumLeft":    "├",     
        "mediumRight":   "┤",    
        "bottomLeft":    "└",    
        "bottomRight":   "┘",    
        "upperMid":      "┬",    
        "midiumMid":     "┼",    
        "bottomMid":     "┴" 
        }
    lines =   {
        "vertical": "│",        
        "horizontal": "─"       
        }

    verticalLine = [lines["horizontal"]*3]*globals.mapSizeX
    verticalUp = corners["upperMid"].join(verticalLine)
    verticalMid = corners["midiumMid"].join(verticalLine)
    verticalDown = corners["bottomMid"].join(verticalLine)
   
    printWhite(corners["upperLeft"]+verticalUp+corners["upperRight"]+"\n")
    for i in range(globals.mapSizeX):
        printWhite(lines["vertical"])
        for j in range(globals.mapSizeY):
            printWhite("   ")
            printWhite(lines["vertical"])            
        print()
        if(i < globals.mapSizeY-1): printWhite(corners["mediumLeft"]+verticalMid+corners["mediumRight"]+"\n")
    printWhite(corners["bottomLeft"]+verticalDown+corners["bottomRight"]+"\n")
"""