class Warrior:
    def __init__(self, health = 100, stamina = 100):
        self.health = health
        self.stamina = stamina
#рассказ героя о себе
    def introduces(self):
        print("---------")
        print(f"Class: {self.__class__.__name__}")
        print(f"Health: {self.health}")
        print(f"Stamina.{self.stamina}")
        print("---------")
#лечение героев
    def heals(self, target):
        print("---------")
        print(f"{self.__class__.__name__} применяет заклинание лечения"
              f" к {target.__class__.__name__}")
        target.health += 10
        self.stamina -= 20
        print(f"Здоровье у {target.__class__.__name__} увеличилось до {target.health}")
        print(f"У {self.__class__.__name__} осталось {self.stamina} единиц магии")
        print("---------")
#атака героя
    def attacks(self, target):
        print("---------")
        print(f"{self.__class__.__name__} наносит урон мечом"
              f" {target.__class__.__name__}")
        target.health -= 3
        print(f"Здоровье у {target.__class__.__name__} понижено до {target.health}")
        print("---------")

class Mage:
    def __init__(self, health = 100, mana = 100):
        self.health = health
        self.mana = mana
#рассказ героя о себе
    def introduces(self):
        print("---------")
        print(f"Class: {self.__class__.__name__}")
        print(f"Health: {self.health}")
        print(f"Mana.{self.mana}")
        print("---------")
#лечение героев
    def heals(self, target):
        print("---------")
        print(f"{self.__class__.__name__} применяет заклинание лечения"
              f" к {target.__class__.__name__}")
        target.health += 10
        self.mana -= 20
        print(f"Здоровье у {target.__class__.__name__} увеличилось до {target.health}")
        print(f"У {self.__class__.__name__} осталось {self.mana} единиц магии")
        print("---------")
#атака героя
    def attacks(self, target):
        print("---------")
        print(f"{self.__class__.__name__} наносит урон магией"
              f" {target.__class__.__name__}")
        target.health -= 3
        print(f"Здоровье у {target.__class__.__name__} понижено до {target.health}")
        print("---------")


unit1 = Warrior(100, 50)
#print("Warrior:",unit1.__dict__)

unit2 = Warrior()
#print("Warrior:",unit2.__dict__)

unit3 = Mage(90, 70)
#print("Mage:", unit3.__dict__)

unit4 = Mage()
#print("Mage:", unit4.__dict__)

#рассказ героя о себе
#unit1.introduces()

#рассказ героя о себе
#unit2.introduces()

#рассказ героя о себе
#unit3.introduces()

#рассказ героя о себе
#unit4.introduces()

#лечение mage
#unit1.heals(unit3)

#лечение mage
#unit3.heals(unit1)

#атака warrior
#unit1.attacks(unit3)

#атака mage
#unit3.attacks(unit1)