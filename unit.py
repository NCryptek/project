import globals

surround = [ #pozycje sąsiednich kratek
     0, -1, #północ
     1,  0, #wschód
     0,  1, #południe
    -1,  0  #zachód
]

warheads = [
    "SA",
    "AT",
    "HE"
]

armors = [
    "LK",
    "CK"
]

dmgEff = [
    [1.0,  0.5 ],
    [0.5,  1.0 ],
    [0.75, 0.75]
]

class PathTile:
    def __init__(self, x, y, cost, parent):
        self.srcX = x
        self.srcY = y
        self.cost = cost
        self.parent = parent
    def __str__(self):
        return f"Pathtile of cost {self.cost} -> ({self.srcX}, {self.srcY})"

class Unit:
    def __init__(self, x, y, template, owner):
        if template == None:
            print("Null unit template\n")
        else:
            self.ownerId = owner
            self.typeId = template.typeId
            self.posX = x
            self.posY = y
            self.health = template.maxHealth
            self.damage = template.damage
            self.range = template.range
            self.speed = template.speed
            self.moveRem = template.speed
            self.damageType = template.damageType
            self.armorType = template.armorType
            globals.tileList[self.posY * globals.mapSizeX + self.posX] = self
        
    def takeDamage(self, dmg, dT):
        try:
            self.health -= (dmg * dmgEff[dT][self.armorType])
        except:
            pass
        #if (self.armorType == 0): #Light
        #    if (dT == 0): #SA
        #        self.health -= dmg
        #    elif (dT == 1): #AT
        #        self.health -= (dmg * 0.5)
        #    elif (dT == 2): #HE
        #        self.health -= (dmg * 0.75)
        #elif (self.armorType == 1): #Heavy
        #    if (dT == 0): #SA
        #        self.health -= (dmg * 0.5)
        #    elif (dT == 1): #AT
        #        self.health -= dmg
        #    elif (dT == 2): #HE
        #        self.health -= (dmg * 0.75)
        if (self.health <= 0):
            self.health = 0
            self.setPos(-1, -1)
        
    def setPos(self, x, y):
        globals.tileList[self.posY * globals.mapSizeX + self.posX] = None
        self.posX = x
        self.posY = y
        if (x > 0 and x < globals.mapSizeX and y > 0 and y < globals.mapSizeY):
          globals.tileList[y * globals.mapSizeX + x] = self

    def moveTo(self, x, y):
        dist = globals.Dist(self.posX, self.posY, x, y)

        if (dist > self.moveRem):
            print("Cannot move to destination, too few moves left")
            return

        if (globals.tileList[y * globals.mapSizeX + x] != self and globals.tileList[y * globals.mapSizeX + x] != None):
            print("Cannot move to destination, already occupied")
            return

        globals.tileList[self.posY * globals.mapSizeX + self.posX] = None
        self.posX = x
        self.posY = y
        globals.tileList[y * globals.mapSizeX + x] = self
        self.moveRem -= dist

    def pathTo(self, x, y):
        if (not globals.IsFreeFor(self, x, y)):
            return []
        #endif
        
        possibleTiles = []
        activeTiles = []
        for i in range(globals.mapSizeY * globals.mapSizeX):
            activeTiles.append(None)
        #endfor

        possibleTiles.append(PathTile(self.posX, self.posY, 0, None)) #pole startowe
        while (len(possibleTiles) > 0):
            curTile = possibleTiles[0] #odwołanie do pierwszego elementu
            if (curTile.srcX == x and curTile.srcY == y): #jeśli jesteśmy u celu
                result = []
                while (curTile.parent != None): #spisywanie ścieżki
                    result.append(curTile)
                    curTile = curTile.parent
                #endwhile
                result.reverse()
                return result
            #endif

            for i in range(4): #sprawdza wszystkie sąsiednie pola
                offX = curTile.srcX + surround[i * 2]
                offY = curTile.srcY + surround[i * 2 + 1]
                if (globals.IsFreeFor(self, offX, offY)): #czy pole jest puste
                    temp = activeTiles[offY * globals.mapSizeX + offX] #zapisanie odwołania do sąsiedniego pola
                    if (temp == None):
                        activeTiles[offY * globals.mapSizeX + offX] = PathTile(offX, offY, curTile.cost + 1, curTile)
                        possibleTiles.append(activeTiles[offY * globals.mapSizeX + offX])
                    elif (temp.cost > curTile.cost + 1):
                        temp.cost = curTile.cost + 1
                        temp.parent = curTile
                    #endif
                #endif
            #endfor
            activeTiles.append(possibleTiles.pop(0))
        #endwhile
        return []
    
    def pathToLimited(self, x, y):
        if (not globals.IsFreeFor(self, x, y)):
            return []
        #endif
        
        possibleTiles = []
        activeTiles = []
        for i in range(globals.mapSizeY * globals.mapSizeX):
            activeTiles.append(None)
        #endfor

        possibleTiles.append(PathTile(self.posX, self.posY, 0, None)) #pole startowe
        while (len(possibleTiles) > 0):
            curTile = possibleTiles[0] #odwołanie do pierwszego elementu
            if (curTile.srcX == x and curTile.srcY == y): #jeśli jesteśmy u celu
                result = []
                while (curTile.parent != None): #spisywanie ścieżki
                    result.append(curTile)
                    curTile = curTile.parent
                #endwhile
                result.reverse()
                return result
            #endif
            if (curTile.cost < self.moveRem):
                for i in range(4): #sprawdza wszystkie sąsiednie pola
                    offX = curTile.srcX + surround[i * 2]
                    offY = curTile.srcY + surround[i * 2 + 1]
                    if (globals.IsFreeFor(self, offX, offY)): #czy pole jest puste
                        temp = activeTiles[offY * globals.mapSizeX + offX] #zapisanie odwołania do sąsiedniego pola
                        if (temp == None):
                            activeTiles[offY * globals.mapSizeX + offX] = PathTile(offX, offY, curTile.cost + 1, curTile)
                            possibleTiles.append(activeTiles[offY * globals.mapSizeX + offX])
                        elif (temp.cost > curTile.cost + 1):
                            temp.cost = curTile.cost + 1
                            temp.parent = curTile
                        #endif
                    #endif
                #endfor
            #endif
            activeTiles.append(possibleTiles.pop(0))
        #endwhile
        return []

class UnitTemplate:
    def __init__(self, name, id, hp, dmg, rng, spd, dT, aT):
        self.displayName = name
        self.typeId = id
        self.maxHealth = hp
        self.damage = dmg
        self.range = rng
        self.speed = spd
        self.damageType = dT
        self.armorType = aT

if (__name__ == "__main__"): #test pathfindingu
    globals.mapSizeX = 10
    globals.mapSizeY = 10
    for i in range(100):
        globals.tileList.append(None)

    tempTemplate = UnitTemplate("", 0, 1, 0, 0, 5, 0, 0)
    tempUnit = Unit(1, 1, tempTemplate, 0)

    pathRes = tempUnit.pathTo(5, 8)
    for i in range(len(pathRes)):
        print(pathRes[i])

#def __init__(self, name, id, hp, dmg, rng, spd, dT, aT):
globals.unitTemplates.append(UnitTemplate("Piechota", 0, 5, 2, 1, 5, 0, 0))
globals.unitTemplates.append(UnitTemplate("Wyrzutnie Rakiet", 1, 3, 5, 1, 4, 1, 0))
globals.unitTemplates.append(UnitTemplate("Pojazd Przeciwpiechotny", 2, 5, 2, 1, 8, 0, 1))
globals.unitTemplates.append(UnitTemplate("Czołg", 3, 6, 4, 1, 2, 2, 1))
globals.unitTemplates.append(UnitTemplate("Działo Przeciwpancerne", 4, 2, 5, 2, 3, 1, 0))
globals.unitTemplates.append(UnitTemplate("Artyleria", 5, 1, 4, 4, 2, 2, 0))
