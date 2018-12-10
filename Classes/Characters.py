from Classes.Entity import *


class Player(Entity):
    def __init__(self, name, max_health=100, weapon='FIST', location=''):
        self.name = name
        self.maxHP = max_health
        self.HP = max_health
        self.weapon = weapon
        self.loc = location
        Entity.__init__(self, self.name)


class Alien(Entity):
    def __init__(self, name, max_health=100, weapon='FIST', location=''):
        self.name = name
        self.maxHP = max_health
        self.HP = max_health
        self.weapon = weapon
        self.loc = location
        Entity.__init__(self, self.name)
