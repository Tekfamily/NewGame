from Classes.Characters import *


Fred = Alien('Fred')
Fred.hurt(50)
print(Fred.HP)
Fred.inv.append(Weapon('Pistol'))
Fred.inv.append(HealthPack(25))
print(Fred.inv)
print(Fred.heal())
