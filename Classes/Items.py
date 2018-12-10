from Classes.Entity import *


class Item(Entity):
    def __init__(self, name):
        self.name = name
        Entity.__init__(self, self.name)


class Weapon(Item):
    def __init__(self, name, ammo, damage):
        self.name = name
        self.ammo = ammo
        self.dmg = damage
        Entity.__init__(self, self.name)


class HealthPacks(Item):
    def __init__(self, name, hp):
        self.name = name
        self.HP = hp
        Entity.__init__(self, self.name)
