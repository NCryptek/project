import globals
import os
import unit
import keyboard
from time import sleep

def setup():
    value = True
    while value:
        os.system("cls")
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
        os.system("cls")
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
        os.system("cls")
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
        
        

