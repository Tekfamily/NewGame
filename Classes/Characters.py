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
        self.inv = []
        Entity.__init__(self, self.name)

    def heal(self):
        if HealthPack in self.inv:
            self.HP += HealthPack.HP
            if self.HP > self.maxHP:
                self.HP = self.maxHP
            print("Healed {} HP\n".format(HealthPack.HP),
                  "You now have {} HP".format(self.HP))
        else:
            print('You have no health packs')

    def hurt(self, damage):
        self.HP -= damage

    def damage(self):
        weapon = Weapon('Pistol')
        weapon.damage()
