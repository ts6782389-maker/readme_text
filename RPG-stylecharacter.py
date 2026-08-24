class Character():
    def __init__(self,name,health,power):
        self.name = name
        self.health = health
        self.power = power

    def is_alive(self):
        if self.health > 0 :
            return True
        else:
            return False

    def attack(self,other):
        other.health -= self.power

class Warrior(Character):
    def __init__(self,name,health,power):
        super().__init__(name,health,power)

    def attack(self,other):
        if self.health > 50:
            damage = self.power+5
            other.health -= damage
            print(self.name,"swings a mighty sword at" , other.name, "for", damage,"damamge!")   
        else:
            super().attack(other)

class Mage(Character):
    def __init__(self,name,health,power,mana):
        super().__init__(name,health,power,)
        self.mana = mana

    def cast_spell(self,other):
        if self.mana >= 10:
            self.mana -= 10
            other.health -= self.power
            print("the magacian uses avakadavra")
        else:
            print("not enough mana")
            super().attack(other)

warrior = Warrior("ragnar",90,30)
mage = Mage("circe",125,15,30)

while warrior.is_alive() and mage.is_alive():
    warrior.attack(mage)
    if not mage.is_alive():
        break
    mage.cast_spell(warrior)


print("the battle is over")
if warrior.is_alive():
    print("the winner" ,warrior.name )
else:
    print("the winner" , mage.name)



       
    
    