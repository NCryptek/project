import globals
import os
import unit
import keyboard
from  colorama import Fore 
from time import sleep

def MapSize():
    value = True
    while value:
        
        clean()
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

def PlayerCount():
    value = True
    while value:
        clean()
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

def clean():
    try: 
        os.system("cls")
    except:
        os.system("clear")

def printWhite(data):
    print(Fore.WHITE,data,end="",sep="")

def printRed(data):
    print(Fore.RED,data,end="",sep="")

def printGreen(data):
    print(Fore.GREEN,data,end="",sep="")

def printScreen():
    clean()
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

def setup():
    MapSize()
    PlayerCount()
    
    value = True
    selects = []
    curOption = 0
    changeTo = -1
    lastKey = ""
    for i in range(globals.startUnitAmt):
        selects.append(i)

    while value:
        clean()
        if (changeTo == -1):
            if (lastKey == "up"): # strzałka w górę
                curOption -= 1
            elif (lastKey == "down"):
                curOption += 1
            elif (lastKey == "enter"):
                if (curOption == globals.startUnitAmt):
                    value = False
            lastKey = ""

            if (curOption < 0):
                curOption = globals.startUnitAmt
            elif (curOption > globals.startUnitAmt):
                curOption = 0

            for i in range(globals.startUnitAmt):
                if (curOption == i):
                    print("> ", end="", sep="")
                else:
                    print("  ", end="", sep="")
                print(f"U-{i + 1}: {globals.unitTemplates[selects[i]].displayName}")
            
            if (curOption == globals.startUnitAmt):
                print("\n> Kontynuuj")
            else:
                print("\n  Kontynuuj")

        
        lastKey = keyboard.read_key()
        sleep(0.05)