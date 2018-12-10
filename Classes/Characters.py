from Classes.Entity import *
from Classes.Items import *
import random


class Player(Entity):
    def __init__(self, name, max_health=100, weapon='Fist', max_damage=10, location=''):
        self.name = name
        self.maxHP = max_health
        self.HP = max_health
        self.weapon = Weapon(weapon)
        self.loc = location
        self.maxDMG = max_damage
        Entity.__init__(self, self.name)

    def take_damage(self, damage):
        self.HP -= damage

    def deal_damage(self):
            self.weapon.damage()


class Alien(Entity):
    def __init__(self, name, max_health=100, weapon='Pistol', max_damage=10, location=''):
        self.name = name
        self.maxHP = max_health
        self.HP = max_health
        self.weapon = Weapon(weapon)
        self.loc = location
        self.maxDMG = max_damage
        Entity.__init__(self, self.name)

    def hurt(self, damage):
        self.HP -= damage

    def damage(self):
        self.weapon.damage()
