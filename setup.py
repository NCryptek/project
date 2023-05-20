import globals
import os
import unit
import keyboard
from time import sleep
def clean():
    try: 
        os.system("cls")
    except:
        return
    try:
        os.system("clear")
    except:
        return    

def setup():
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

    #tworzenie mapy TODO

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
        
"""
def printMap():
    os.system('clear')
    corners = {
               "upperLeft":     "┌",    #218 np. chr(218)
               "upperRight":    "┐",    #191
               "mediumLeft":    "├",    #195 
               "mediumRight":   "┤",    #180
               "bottomLeft":    "└",    #192
               "bottomRight":   "┘",    #217
               "upperMid":      "┬",    #194
               "midiumMid":     "┼",    #197
               "bottomMid":     "┴"     #193
              }
    lines =   {
               "vertical": "│",         #179
               "horizontal": "─"        #196
              }
    
    

    verticalLine = [lines["horizontal"]*3]*globals.mapSizeX        
    verticalUp = corners["upperMid"].join(verticalLine)
    verticalMid = corners["midiumMid"].join(verticalLine)
    verticalDown = corners["bottomMid"].join(verticalLine)

   
    print(corners["upperLeft"]+verticalUp+corners["upperRight"])
    for i in range(globals.mapSizeY-1):
        for j in range(globals.mapSizeX):
            print(lines["vertical"], end="")  
            print("   ", end="")
        print(lines["vertical"]) 
        if(i < globals.mapSizeX-1): print(corners["mediumLeft"]+verticalMid+corners["mediumRight"])
    for j in range(globals.mapSizeX):
        print(lines["vertical"], end="")  
        print("   ", end="")
    print(lines["vertical"]) 
    print(corners["bottomLeft"]+verticalDown+corners["bottomRight"])
"""