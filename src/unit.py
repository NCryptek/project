import globals

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
        result = []
        if (not globals.IsFreeFor(self, x, y)):
            return None
        
        


        return result

class UnitTemplate:
    def __init__(self, id, hp, dmg, rng, spd, dT, aT):
        self.typeId = id
        self.maxHealth = hp
        self.damage = dmg
        self.range = rng
        self.speed = spd
        self.damageType = dT
        self.armorType = aT
