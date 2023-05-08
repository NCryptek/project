import globals
def setup():
    value = True
    while value:
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
        print("Podaj OSOBNO ORAZ KOLEJNO ilość graczy (1-4) i ilość jednostek na gracza (1-5)")
        playerCount = input()
        armySize = input()
        try:
            globals.playerAmt = int(playerCount)
            globals.startUnitAmt = int(armySize)
        except:
            continue
        if (playerCount<1 or playerCount > 4):
            continue
        if (armySize<1 or armySize>5):
            continue
        value = False
