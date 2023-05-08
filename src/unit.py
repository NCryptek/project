class Unit:
    def __init__(self, template, owner):
        if template == None:
            print("Null unit template\n")
        else:
            self.ownerId = owner
            self.typeId = template.typeId
            self.health = template.maxHealth
            self.damage = template.damage
            self.range = template.range
            self.speed = template.speed
            self.moveRem = template.speed
            self.damageType = template.damageType
            self.armorType = template.armorType
        
    def takeDamage(self, dmg, dT):
        return
    def setPos(self, x, y):
        return
    def moveTo(self, x, y):
        return

class UnitTemplate:
    def __init__(self, id, hp, dmg, rng, spd, dT, aT):
        self.typeId = id
        self.maxHealth = hp
        self.damage = dmg
        self.range = rng
        self.speed = spd
        self.damageType = dT
        self.armorType = aT
