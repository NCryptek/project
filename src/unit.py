import globals

surround = [ #pozycje sąsiednich kratek
     0, -1, #północ
     1,  0, #wschód
     0,  1, #południe
    -1,  0  #zachód
]

class PathTile:
    def __init__(self, x, y, cost, parent):
        self.srcX = x
        self.srcY = y
        self.cost = cost
        self.parent = parent

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
        
    def takeDamage(self, dmg, dT):
        if (self.armorType == 0): #Light
            if (dT == 0): #SA
                self.health -= dmg
            elif (dT == 1): #AT
                self.health -= (dmg * 0.5)
            elif (dT == 2): #HE
                self.health -= (dmg * 0.75)
        elif (self.armorType == 1): #Heavy
            if (dT == 0): #SA
                self.health -= (dmg * 0.5)
            elif (dT == 1): #AT
                self.health -= dmg
            elif (dT == 2): #HE
                self.health -= (dmg * 0.75)
        
    def setPos(self, x, y):
        globals.tileList[self.posY * globals.mapSizeX + self.posX] = None
        self.posX = x
        self.posY = y
        globals.tileList[y * globals.mapSizeX + x] = self

    def moveTo(self, x, y):
        dist = globals.Dist(self.x, self.y, x, y)

        if (dist > self.moveRem):
            print("Cannot move to destination, too little moves left")
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
        for i in range(globals.mapSizeY * globals.mapSizeX):
            possibleTiles.append(None)
        #endfor

        possibleTiles.append(PathTile(self.x, self.y, 0, None)) #pole startowe
        while (len(possibleTiles) > 0):
            curTile = possibleTiles[0] #odwołanie do pierwszego elementu

            if (curTile.srcX == x and curTile.srcY == y): #jeśli jesteśmy u celu
                result = []
                while (curTile.parent != None): #spisywanie ścieżki
                    result.append(curTile)
                    curTile = curTile.parent
                #endwhile
                return result
            #endif

            for i in range(4): #sprawdza wszystkie sąsiednie pola
                offX = curTile.srcX + surround[i * 2]
                offY = curTile.srcY + surround[i * 2 + 1]
                if (globals.IsFreeFor(self, offX, offY)): #czy pole jest puste
                    temp = possibleTiles[offY * globals.mapSizeX + offX] #zapisanie odwołania do sąsiedniego pola
                    if (temp == None):
                        possibleTiles[offY * globals.mapSizeX + offX] = PathTile(offX, offY, curTile.cost + 1, curTile)
                    elif (temp.cost > curTile.cost + 1):
                        temp.cost = curTile.cost + 1
                        temp.parent = curTile
                    #endif
                #endif
            #endfor
            possibleTiles.pop(0)
        #endwhile
        return []

class UnitTemplate:
    def __init__(self, id, hp, dmg, rng, spd, dT, aT):
        self.typeId = id
        self.maxHealth = hp
        self.damage = dmg
        self.range = rng
        self.speed = spd
        self.damageType = dT
        self.armorType = aT
PiechotaTemplate = UnitTemplate(1, 5, 2, 1, 5, 0, 0)
RocketTemplate = UnitTemplate(2, 3, 5, 1, 4, 1, 0)
PPTemplate = UnitTemplate(3, 5, 2, 1, 8, 0, 1)
TankTemplate = UnitTemplate(4, 6, 4, 1, 2, 2, 1)
DPTemplate = UnitTemplate(5, 2, 5, 2, 3, 1, 0)
ArtileryTemplate = UnitTemplate(6, 1, 4, 4, 2, 2, 0)