from Classes.Entity import *
import random


class Item(Entity):
    def __init__(self, name):
        self.name = name
        Entity.__init__(self, self.name)


class Weapon(Item):
    def __init__(self, name):
        self.name = name
        Entity.__init__(self, self.name)

        if self.name == 'Fist':
            self.ammo = 0
        if self.name == 'Pistol':
            self.ammo = 0
        if self.name == 'Rifle':
            self.ammo = 0

    def damage(self):
        dmg = 0
        if self.name == 'Fist':
            if self.ammo == 0:
                for i in range(1):
                    dmg += random.randint(1, 10)
                return dmg
            else:
                return False

        elif self.name == 'Pistol':
            if self.ammo > 0:
                for i in range(2):
                    dmg += random.randint(1, 10)
                    self.ammo -= 1
                return dmg
            else:
                return False

        elif self.name == 'Rifle':
            if self.ammo > 0:
                for i in range(3):
                    dmg += random.randint(1, 10)
                    self.ammo -= 1
                return dmg
            else:
                return False


class HealthPacks(Item):
    def __init__(self, name, hp):
        self.name = name
        self.HP = hp
        Entity.__init__(self, self.name)
